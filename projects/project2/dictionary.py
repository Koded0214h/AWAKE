todo = {
    "Work": [],
    "Personal": [],
    "Others": []
}

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
def add_task(todo):
    category = input(f"Enter category ({todo.keys()}): ")
    
    if category not in todo:
        todo[category] = []
        
    task = input("Enter task: ")
    todo[category].append(task)
    
    print("✅ Task added successfully!")
    
def view_task(todo):
    for category, tasks in todo.items():
        print(f"{category}: ")
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f" {i}. {task}")
        else:
            print("No tasks")
                
                
def delete_task(todo):
    category = input(f"Enter category {todo.keys()}: ")
    
    if category in todo.keys():
        
        tasks = todo[category]
        
        if tasks:
        
            for i, task in enumerate(tasks, start=1):
                print(f" {i}. {task}")
            num = int(input("Enter task number to delete: ")) -1
            
            if  0 <= num < len(tasks):
                removed = tasks.pop(num)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number!")
        else:
            print("Empty Tasks")
    else: 
        print("No such category exists!")
        

    
while True:
    show_menu()
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_task(todo)
    elif choice == "2":
        view_task(todo)
    elif choice == "3":
        delete_task(todo)
    elif choice == "4":
        print("Exiting.......")
        break
    else:
        print("Number not recognised!")

# Assignment on Dictionary ToDo List
# ==================================
# 1. Upgrade the project
# 2. Add an update function