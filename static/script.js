
document.addEventListener("DOMContentLoaded", () => {
    const taskForm = document.querySelector(".task-form");
    const taskInput = taskForm?.querySelector('input[name="title"]');
    const addButton = taskForm?.querySelector('button[type="submit"]');

    taskForm?.addEventListener("submit", (event) => {
        if (!taskInput.value.trim()) {
            event.preventDefault();
            taskInput.focus();
            return;
        }

        addButton.disabled = true;
        addButton.textContent = "Adding...";
    });

    document.querySelectorAll(".task-item").forEach((task) => {
        task.addEventListener("mouseenter", () => {
            task.style.backgroundColor = "#fafaff";
        });

        task.addEventListener("mouseleave", () => {
            task.style.backgroundColor = "";
        });
    });
});