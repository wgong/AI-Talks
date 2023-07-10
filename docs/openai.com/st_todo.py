import streamlit as st
from pathlib import Path 

TODO_FILENAME = "todos.txt"

def add_todo():
    todo = st.text_input("Enter a new to-do item:")

    if st.button("Add"):
        with open(TODO_FILENAME, "a") as file:
            file.write(todo + "\n")
            st.success("To-do item added successfully!")

def show_todos():
    if not Path(TODO_FILENAME).exists():
        return 
    
    st.header("To-Do List:")
    with open(TODO_FILENAME, "r") as file:
        todos = file.readlines()
        for i, todo in enumerate(todos):
            st.write(f"{i + 1}. {todo.strip()}")

def main():
    st.title("To-Do List Manager")

    add_todo()
    show_todos()

if __name__ == "__main__":
    main()