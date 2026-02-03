tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!") 
    elif choice == "2":
        if not tasks:
            print("No tasks added yet.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    elif choice == "3":
        print("Goodbye! Have a productive day.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


