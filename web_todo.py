import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local+'\n')
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This app will increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


todo = st.text_input(label="Enter Todo",
                     placeholder="Add a todo",
                     on_change=add_todo,
                     key='new_todo')
