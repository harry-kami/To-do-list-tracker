import json
import os
from datetime import datetime

tasks = []
TASKS_FILE = "tasks.json"

# -------------------------------
# JSON Saving and Loading
# -------------------------------
def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# -------------------------------
# Task Functions
# -------------------------------

# Add new task
def add_task():
    title = input("Enter new task: ")
    now = datetime.now().isoformat(timespec='seconds')
    task = {
        "title": title,
        "status": "not done",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(task)
    save_tasks()
    print(f"Task added: {title}")

# Get emoji for a status
def get_status_emoji(status):
    return {"done": "✅", "in progress": "⏳", "not done": "❌"}.get(status, "")

# View tasks (optionally filtered)
def view_tasks(status=None):
    filtered = tasks if status is None else [t for t in tasks if t["status"] == status]
    if not filtered:
        print("\nNo tasks found.")
        return

    header = "All" if not status else status.capitalize()
    print(f"\n{header} Tasks:")
    for i, t in enumerate(filtered, start=1):
        emoji = get_status_emoji(t["status"])
        print(f"{i}. {t['title']} — {t['status']} {emoji}")
        print(f"   Created: {t['createdAt']}, Updated: {t['updatedAt']}")

# Change task status
def change_task_status():
    view_tasks()
    try:
        index = int(input("Select task number: ")) - 1
        if 0 <= index < len(tasks):
            print("\n1. ✅ Done")
            print("2. ⏳ In-progress")
            print("3. ❌ Not done")
            choice = input("Select new status: ")

            if choice == "1":
                tasks[index]["status"] = "done"
            elif choice == "2":
                tasks[index]["status"] = "in progress"
            elif choice == "3":
                tasks[index]["status"] = "not done"
            else:
                print("Invalid choice.")
                return

            tasks[index]["updatedAt"] = datetime.now().isoformat(timespec='seconds')
            save_tasks()
            print(f"Updated: {tasks[index]['title']} — {tasks[index]['status']} {get_status_emoji(tasks[index]['status'])}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Task options
def task_options():
    print("\n1. View completed tasks")
    print("2. View tasks not done")
    print("3. View tasks in progress")
    choice = input("Select option (1,2,3): ")
    if choice == "1":
        view_tasks("done")
    elif choice == "2":
        view_tasks("not done")
    elif choice == "3":
        view_tasks("in progress")
    else:
        print("Invalid input.")

# Delete task
def delete_task():
    view_tasks()
    try:
        index = int(input("Select the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            task_title = tasks[index]['title']
            confirm = input(f"Are you sure you want to delete '{task_title}'? (y/n): ").lower()
            if confirm == "y":
                tasks.pop(index)
                save_tasks()
                print(f"Task '{task_title}' has been deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# -------------------------------
# Main Program
# -------------------------------
print("Welcome to the Task Tracker 📝")
load_tasks()

while True:
    print("\n--Options--")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Task options")
    print("4. Edit task status")
    print("5. Delete a task")
    print("6. Exit")

    user_input = input("Select an option (1-6): ")
    if user_input == "1":
        view_tasks()
    elif user_input == "2":
        add_task()
    elif user_input == "3":
        task_options()
    elif user_input == "4":
        change_task_status()
    elif user_input == "5":
        delete_task()
    elif user_input == "6":
        print("Exiting task tracker... 👋")
        break
    else:
        print("Invalid input.")
