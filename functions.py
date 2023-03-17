FILEPATH = "todos.txt"


def get_todos(filepath: str = FILEPATH):
    """This function used to get the todo from the text file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local: list[str], op: chr = 'w', filepath: str = FILEPATH):
    """This function used to write , edit and remove todo from the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)
    if op == 'a':
        print("New todo added successfully")
    elif op == 'c':
        print("Todo marked as completed and removed from the list")
    elif op == 'e':
        print("Todo update has completed successfully")
    return


if __name__ == "__main__":
    print(get_todos())
