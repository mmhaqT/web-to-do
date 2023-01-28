import streamlit as ST
import functions

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
ST.markdown(hide_streamlit_style, unsafe_allow_html=True)

todos = functions.get_todos()


def add_todo():
    todo = "\n" + ST.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)


ST.title("My WebTodo App")
ST.subheader("This is my todo app.")
ST.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
   checkbox = ST.checkbox(todo, key=todo)
   if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del ST.session_state[todo]
       ST.experimental_rerun()

ST.text_input(label="Enter Todo:", placeholder="Enter a Todo...",
              on_change=add_todo, key="new_todo")

# print("Hello")
# ST.session_state



