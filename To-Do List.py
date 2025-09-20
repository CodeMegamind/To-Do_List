import customtkinter as ctk
from customtkinter import CTkButton

app= ctk.CTk()

app.geometry("400x500")
app.title("To-Do List")

frame1 = ctk.CTkFrame(app, )
frame1.pack(fill="x")

bbl = ctk.CTkEntry(frame1, placeholder_text="Task Name")
bbl.pack(side="left", fill="x", expand=True)

def add_task ():
    print("Adding Task")
    task_frame = ctk.CTkFrame(bbc, fg_color="#2e2e2e")
    task_frame.pack(fill="x")
    task_checkbox = ctk.CTkCheckBox(task_frame, text=bbl.get())
    task_checkbox.pack(side="left")
    task_button = ctk.CTkButton(task_frame, text="×", width=50)
    task_button.pack(side="right")


btn_1 =ctk.CTkButton(frame1, text="Add Task", command=add_task)
btn_1.pack(side="left", fill="x", expand=True)

bbc = ctk.CTkScrollableFrame(app)
bbc.pack(fill="both", expand=True)






















































app.mainloop()