import streamlit as st

# Create a list to store the to-do items
todos = []

# Function to add a new to-do item
def add_todo():
    todo = st.text_input("Enter a new to-do item:")
    if st.button("Add"):
        todos.append(todo)
        st.success("To-do item added successfully!")

# Function to display the to-do list
def show_todos():
    st.header("To-Do List:")
    for i, todo in enumerate(todos):
        st.write(f"{i + 1}. {todo}")

# Main function to run the app
def main():
    st.title("To-Do List Manager")

    add_todo()
    show_todos()

if __name__ == "__main__":
    main()