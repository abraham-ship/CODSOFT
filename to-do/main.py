print('To-do app!')

tasks = []

def create_task():
    print("\nCreating a new task")
    task = input("What task do you want to add: ")
    if task.strip():
        tasks.append(task)
        print("Task added successfully")
    else:
        print("Task cannot be empty. Please enter a valid task.")

def edit_task():
    print('\nEditing a task...')
    show_all()

    try:
        index = int(input('Enter the number of the task you want to edit: ')) - 1
        if 0 <= index < len(tasks):
            new_task = input('Enter the new task: ')
            tasks[index] = new_task
            print('Task edited successfully.')
        else:
            print('Invalid task number. No task edited.')
    except ValueError:
        print('Invalid input. Please enter a valid number.')

def show_all():
    if not tasks:
        print("You have no tasks")
    else:
        print("\nThese are your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    print("\nDeleting tasks")
    if not tasks:
        print("Nothing to delete here")
        return

    show_all()

    try:
        idx = int(input('Please enter the task number to be deleted: '))
        if 1 <= idx <= len(tasks):
            deleted_task = tasks.pop(idx - 1)
            print(f'Task "{deleted_task}" deleted successfully.')
        else:
            print("Invalid index, please try again")
    except ValueError:
        print('Invalid input. Please enter a valid number.')

def exit_app():
    print("Exiting the ToDo app. Goodbye!")
    exit()

options = {
    '1': create_task,
    '2': show_all,
    '3': edit_task,
    '4': delete_task,
    '5': exit_app
}

def main():
    while True:
        print("\nOptions:")
        print("1. Create Task")
        print("2. Show All Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter the number of your choice (1-5): ")

        selected_option = options.get(choice)
        if selected_option:
            selected_option()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the ToDo app
if __name__ == "__main__":
    main()
