
import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DB_DIR = os.path.join(app.root_path, "instance")
DB_PATH = os.path.join(DB_DIR, "tasks.db")
os.makedirs(DB_DIR, exist_ok=True)


def get_db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                priority TEXT NOT NULL DEFAULT 'Medium',
                status TEXT NOT NULL DEFAULT 'Pending'
            )
        """)


@app.route("/")
def index():
    with get_db() as db:
        tasks = db.execute(
            "SELECT * FROM tasks ORDER BY id DESC"
        ).fetchall()

    total = len(tasks)
    completed = sum(t["status"] == "Completed" for t in tasks)
    pending = total - completed
    progress = round(completed * 100 / total) if total else 0

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending,
        progress=progress
    )


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    priority = request.form.get("priority", "Medium")

    if not title or len(title) > 120:
        return "Task title must contain 1–120 characters.", 400

    if priority not in ("Low", "Medium", "High"):
        return "Invalid priority.", 400

    with get_db() as db:
        db.execute(
            "INSERT INTO tasks (title, priority) VALUES (?, ?)",
            (title, priority)
        )

    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    with get_db() as db:
        db.execute("""
            UPDATE tasks
            SET status = CASE
                WHEN status = 'Pending' THEN 'Completed'
                ELSE 'Pending'
            END
            WHERE id = ?
        """, (task_id,))

    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    with get_db() as db:
        db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    return redirect(url_for("index"))


@app.route("/health")
def health():
    try:
        with get_db() as db:
            db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}, 200
    except sqlite3.Error:
        return {"status": "unhealthy", "database": "error"}, 503


init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)