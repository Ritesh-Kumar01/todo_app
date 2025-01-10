from tabulate import tabulate
from colorama import Fore,Style
from utilts import line
from db import get_connection
from crud import view_task,view_single_task,add_task,update_task,delete_task

def show_options():
    print("1. View task")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit the program")



def match_cases(user_input):
    match user_input:
        case 1:
            print("View task")
            rows = view_task()
            if rows:
                head = ["TodoId", "Todo Name","Todo Desc","CreatedAt","Status"]
                # applying color over status 
                colored_row = []
                for row in rows:
                    status = row[4]
                    if status.lower() == "completed":
                        colored_status = f"{Fore.GREEN}{status}{Style.RESET_ALL}"
                    else:
                        colored_status = f"{Fore.RED}{status}{Style.RESET_ALL}"
                    
                    new_row = list(row[:4]) + [colored_status]
                    colored_row.append(new_row)

                # priniting table
                print(tabulate(colored_row, headers=head, tablefmt="grid"))


            else:
                print("No Task found.")

        case 2:
            print("Add task")
            task_name = input("Enter your task name : ")
            task_desc = input("Enter your task desc : ")
            add_task(task_name,task_desc)
            print("Data inserted successfully.")

        case 3:
            print("Update task")
            task_id = int(input("Enter your todo id : "))
            row = view_single_task(task_id)
            print(row)
            print("Your Old Data ")
            print(f"\t Task Name : {row[1]}")
            print(f"\t Task Desc : {row[2]}")
            # adding new data
            new_task_name = input("Enter your new task name : ")
            new_task_desc = input("Enter your new task desc : ")
            new_task_status = int(input("Choose 0 for Not Completed and 1 for Completed : "))
            rowcount = update_task(row[0],new_task_name,new_task_desc,new_task_status)
            if rowcount == 0:
                print("No task found with the given ID.")
            else:
                print("Task updated successfully!")
            print("Data inserted successfully.")


        case 4:
            print("Delete task")
            task_id = int(input("Enter your todo id : "))
            total_row = delete_task(task_id)
            if total_row == 0:
                print("No such row exists.")
            else:
                print("Data deleted successfully.")

        case _:
            print("Invalid input, Please choose correct option.")

def main():
    try:
        con = get_connection()
        print("db connected successfully")
        
    except Exception as e:
        print(f"Getting Error : {e}")


    line()
    print("Welcome to todo app 👍")

    while True:
        try:
            show_options()
            user_input = int(input("Please enter a number to choose : "))
            if user_input == 5:
                break
            else:
                match_cases(user_input)
        except ValueError:
            print("Please enter a correct value.")
        
    line()
    print("Thanks for using app. 👍")




if __name__ == "__main__":
    main()