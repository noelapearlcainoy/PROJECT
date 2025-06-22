import tkinter as tk
from tkinter import font

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.configure(bg="#000000")
        self.root.geometry("550x500")

        self.tasks = []
        self.editing_index = None

        self.create_title()

    def create_title(self):
        title = tk.Label(self.root, text="Todo List", font=("Helvetica", 22, "bold"), bg="#000000", fg="white")
        title.pack(pady=10)

        input_frame = tk.Frame(self.root, bg="#000000")
        input_frame.pack(pady=10, fill="x", padx=10)

        self.task_entry = tk.Entry(input_frame, font=("Arial", 14), width=30, fg="black", bg="white", insertbackground="white")
        self.task_entry.pack(side="left", padx=5, fill="x", expand=True)

        self.add_btn = tk.Button(input_frame, text="Add Task", font=("Arial", 12, "bold"), width=10, bg="#1100FD", fg="white", bd=2, command=self.add_or_update_task)
        self.add_btn.pack(side="right", padx=5)

        self.counter_label = tk.Label(self.root, text="Total Tasks: 0 | Completed: 0", font=("Arial", 12), bg="#000000", fg="white")
        self.counter_label.pack()

        self.list_frame = tk.Frame(self.root, bg="#000000")
        self.list_frame.pack(pady=10, fill="both", expand=True)

    def add_or_update_task(self):
        task = self.task_entry.get()
        if task:
            if self.editing_index is None:
                self.tasks.append(task)
            else:
                self.tasks[self.editing_index] = task
                self.editing_index = None
                self.add_btn.config(text="Add Task")
            self.task_entry.delete(0, tk.END)
            self.update_list()

    def prepare_edit(self, index):
        self.editing_index = index
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(0, self.tasks[index].replace("[COMPLETED] ", ""))
        self.add_btn.config(text="Update Task")

    def complete_task(self, index):
        if not self.tasks[index].startswith("[COMPLETED] "):
            self.tasks[index] = f"[COMPLETED] {self.tasks[index]}"
            self.update_list()

    def delete_task(self, index):
        del self.tasks[index]
        if self.editing_index == index:
            self.editing_index = None
            self.add_btn.config(text="Add Task")
        self.update_list()

    def update_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        completed_count = 0  

        for idx, task in enumerate(self.tasks):
            frame = tk.Frame(self.list_frame, bg="#000000", highlightbackground="#e4127b", highlightthickness=1)
            frame.pack(fill="x", pady=5, padx=5)

            is_completed = task.startswith("[COMPLETED] ")
            if is_completed:
                completed_count += 1

            display_text = task.replace("[COMPLETED] ", "") if is_completed else task

            task_font = font.Font(family="Arial", size=12)
            if is_completed:
                task_font.configure(overstrike=1)
                label_fg = "#888888"
            else:
                label_fg = "white"

            label = tk.Label(frame, text=display_text, font=task_font, bg="#000000", fg=label_fg)
            label.pack(side="left", padx=5)

            edit_btn = tk.Button(frame, text="EDIT", fg="#00ffaa", bg="#000000", bd=0, command=lambda i=idx: self.prepare_edit(i))
            complete_btn = tk.Button(frame, text="COMPLETED", fg="#ffa500", bg="#000000", bd=0, command=lambda i=idx: self.complete_task(i))
            delete_btn = tk.Button(frame, text="DELETE", fg="#ff0055", bg="#000000", bd=0, command=lambda i=idx: self.delete_task(i))

            delete_btn.pack(side="right", padx=5)
            complete_btn.pack(side="right", padx=5)
            edit_btn.pack(side="right", padx=5)

       
        self.counter_label.config(text=f"Total Tasks: {len(self.tasks)} | Completed: {completed_count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()
