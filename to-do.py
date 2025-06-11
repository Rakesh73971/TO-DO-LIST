def print_menu():
    print("TO DO LIST")
    print("1.Display tasks")
    print("2.Add task")
    print("3.remove task")
    print("4.Exit")

def get_choice():
    while True:
        valid_choice=("1","2","3","4")
        choice=input("Enter your choice: ")
        if choice not in valid_choice:
            print("Invalid choice")
            continue
        else:
            return choice
def display_tasks(tasks):
    if not tasks:
        print("No tasks in list")
        return 
    for index,task in enumerate(tasks,start=1):
        print(f"{index},{task}")

def add_task(tasks):
    while True:
        task=input("Enter a task: ").strip()
        if len(task) != 0:
            tasks.append(task)
            break
        else:
            print("Invalid task")

def remove_task(tasks):
    display_tasks(tasks)

    while True:
        try:
            task_number=int(input("Enter task number: "))
            if 1<=task_number<=len(tasks):
                tasks.pop(task_number-1)
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid task number")
def main():
    tasks=[]

    while True:
        print_menu()

        choice=get_choice()

        if choice=="1":
            display_tasks(tasks)
        elif choice=="2":
            add_task(tasks)
        elif choice=="3":
            remove_task(tasks)
        elif choice=="4":
            break

if __name__=="__main__":
    main()

    

