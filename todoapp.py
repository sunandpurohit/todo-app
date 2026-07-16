"""
Simple To-Do List Application
Author: Sunand Purohit
Description: A command-line to-do list manager that lets you add, view, complete, and delete tasks.
Tasks are saved to a file so they persist between sessions.
"""

import json
import os
from datetime import datetime

# File where tasks are stored
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file. Return empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)
    print("✓ Tasks saved!")

def add_task(tasks):
    """Add a new task."""
    task_name = input("\nEnter task description: ").strip()
    if not task_name:
        print("⚠ Task cannot be empty!")
        return
    
    task = {
        "id": len(tasks) + 1,
        "name": task_name,
        "completed": False,
        "created_on": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    print(f"✓ Task added: '{task_name}'")
    save_tasks(tasks)

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n📭 No tasks yet! Add one to get started.")
        return
    
    print("\n" + "="*60)
    print("YOUR TASKS")
    print("="*60)
    for task in tasks:
        status = "✓ DONE" if task["completed"] else "⏳ TODO"
        print(f"[{task['id']}] {status} | {task['name']}")
        print(f"    Created: {task['created_on']}")
    print("="*60)

def mark_complete(tasks):
    """Mark a task as completed."""
    if not tasks:
        print("⚠ No tasks to complete!")
        return
    
    view_tasks(tasks)
    try:
        task_id = int(input("\nEnter task ID to mark complete: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"✓ Task '{task['name']}' marked as complete!")
                save_tasks(tasks)
                return
        print("⚠ Task ID not found!")
    except ValueError:
        print("⚠ Please enter a valid number!")

def delete_task(tasks):
    """Delete a task."""
    if not tasks:
        print("⚠ No tasks to delete!")
        return
    
    view_tasks(tasks)
    try:
        task_id = int(input("\nEnter task ID to delete: "))
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                deleted_name = task["name"]
                tasks.pop(i)
                print(f"✓ Task '{deleted_name}' deleted!")
                save_tasks(tasks)
                return
        print("⚠ Task ID not found!")
    except ValueError:
        print("⚠ Please enter a valid number!")

def show_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("📋 TO-DO LIST MANAGER")
    print("="*60)
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print("="*60)

def main():
    """Main application loop."""
    print("\n🚀 Welcome to To-Do List Manager!")
    
    tasks = load_tasks()
    if tasks:
        print(f"✓ Loaded {len(tasks)} task(s) from last session.")
    
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\n👋 Goodbye! Your tasks are saved.")
            break
        else:
            print("⚠ Invalid option! Please choose 1-5.")

if __name__ == "__main__":
    main()
