"""
Task Manager Project (Pro Version with JSON)
Author: Mohamed Abdelrazek
Course: Programming in Python by Meta (Coursera)

Description:
------------
This is a simple Task Manager program built using Python fundamentals.
It demonstrates the following skills learned in the course:
- Variables and Data Types
- Lists, Dictionaries
- Functions
- Loops and Conditional Statements
- File Handling (Saving and Loading Tasks with JSON)
- Error Handling (try/except)
- Input/Output

The program allows the user to:
1. Add a task
2. View all tasks
3. Mark a task as completed
4. Delete a task
5. Save and load tasks from a JSON file
6. Exit the program
"""

import json

# ===================== #
#   GLOBAL VARIABLES    #
# ===================== #
tasks = []   # A list to store tasks. Each task will be a dictionary.


# ===================== #
#   FUNCTIONS           #
# ===================== #

def show_menu():
    """Displays the main menu options to the user."""
    print("\n--- Task Manager ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Save tasks to file")
    print("6. Load tasks from file")
    print("7. Exit")


def add_task():
    """Adds a new task to the tasks list."""
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    print(f"Task '{title}' added successfully!")


def view_tasks():
    """Displays all tasks with their status."""
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✔ Completed" if task["completed"] else "❌ Not Completed"
            print(f"{index}. {task['title']} - {task['description']} [{status}]")


def mark_task_completed():
    """Marks a chosen task as completed."""
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task '{tasks[task_number - 1]['title']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    """Deletes a chosen task."""
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def save_tasks():
    """Saves all tasks to a JSON file."""
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
        print("Tasks saved successfully to 'tasks.json'.")
    except Exception as e:
        print("Error saving tasks:", e)


def load_tasks():
    """Loads tasks from a JSON file."""
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        print("Tasks loaded successfully from 'tasks.json'.")
    except FileNotFoundError:
        print("No saved file found. Please save tasks first.")
    except Exception as e:
        print("Error loading tasks:", e)


# ===================== #
#   MAIN PROGRAM LOOP   #
# ===================== #

def main():
    """Runs the main program loop."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            load_tasks()
        elif choice == "7":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
