import os
import sys
import json

FILE_NAME = "task.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)


def main_menu():
    tasks = load_tasks()
    while True:
        print("To Do List CLI App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. edit Tasks")
        print("4. Mark Task as Done")
        print("5. Unmark Task")
        print("6. Delete Task")
        print("7. Exit")
        choice = input("Choose Menu: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)
            print("Task added successfully!")
            input("Press Enter to continue...")
            print(" ")
        elif choice == "2":
            print("remaining tasks", len(tasks))
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['task']} {'(done)' if task['done'] else ''}")
            input("Press Enter to continue...")
            print(" ")

        elif choice == "3":
            index = int(input("Enter task number: ")) - 1
            if index < 0 or index >= len(tasks):
                print("Invalid task number.")
                input("Press Enter to continue...")
                print(" ")
                continue
            new_task = input("Enter new task: ")
            tasks[index]["task"] = new_task
            save_tasks(tasks)
            print("Task edited successfully!")
            input("Press Enter to continue...")
            print(" ")
            
        elif choice == "4":
            index = int(input("Enter task number: ")) - 1
            if index < 0 or index >= len(tasks):
                print("Invalid task number.")
                input("Press Enter to continue...")
                print(" ")
                continue
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
            input("Press Enter to continue...")
            print(" ")
        
        elif choice == "5":
            index = int(input("Enter task number: ")) - 1
            if index < 0 or index >= len(tasks):
                print("Invalid task number.")
                input("Press Enter to continue...")
                print(" ")
                continue
            tasks[index]["done"] = False
            save_tasks(tasks)
            print("Task unmarked successfully!")
            input("Press Enter to continue...")
            print(" ")
    
        elif choice == "6":
            index = int(input("Enter task number: ")) - 1
            if index < 0 or index >= len(tasks):
                print("Invalid task number.")
                input("Press Enter to continue...")
                print(" ")
                continue
            tasks.pop(index)
            save_tasks(tasks)
            print("Task deleted successfully!")
            input("Press Enter to continue...")
            print(" ")

        elif choice == "7":
            sys.exit("Goodbye!")
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()