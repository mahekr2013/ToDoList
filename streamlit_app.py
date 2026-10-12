import streamlit as st
st.title("To-Do List")
st.subheader("Welcome to To-Do List! This program will help you track your daily tasks.")

if "tasks" not in st.session_state:
    st.session_state["tasks"]=[]
with st.container(border = True):
    st.subheader("Tasks for today:")
    for i in range(len(st.session_state["tasks"])):
        st.write(str(i+1) + ". " + str(st.session_state["tasks"][i]))

col1,col2 = st.columns(2)
with col1:
    with st.container(border = True):
        task = st.text_input("Enter a task you would like to add to your to-do list: ")
        if st.button("add"):
            if task != "":
                st.session_state["tasks"].append(task)
                st.write("The task has been added!")

with col2:
    with st.container(border = True):       
        remove = st.text_input("Enter what task you would like to remove")
        if st.button("remove"):
            if remove != "":
                st.session_state["tasks"].remove(remove)
                st.write("The task has been removed")




