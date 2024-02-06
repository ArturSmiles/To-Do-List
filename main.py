import customtkinter as ctk


class toDoList:
    def __init__(self) -> None:
        self.app = ctk.CTk()
        self.app.geometry("455x275")
        self.app.title("To-Do List")
        ctk.set_appearance_mode("dark")

        self.frame = ctk.CTkFrame(master=self.app)
        self.frame.grid(column=0, row=0, sticky=("nsew"))

        self.entry = ctk.CTkEntry(
            self.frame, placeholder_text="Task", width=380)
        self.entry.grid(column=0, row=0, pady=10, padx=(10, 2), sticky="nsew")

        self.scrollable_frame = ctk.CTkScrollableFrame(self.frame, width=400)
        self.scrollable_frame.grid(column=0, row=1, columnspan=2,
                                   padx=(10, 10), sticky="nsew")

        self.submit = ctk.CTkButton(self.frame, text="submit",
                                    command=self.submitText, width=10)
        self.submit.grid(column=1, row=0, pady=10, padx=(2, 10), sticky="e")

        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1)
        self.app.resizable(False, False)

        self.tasks = {}
        self.del_buttons = {}
        self.labels = {}

        self.app.mainloop()

    def delete(self, text):
        self.del_buttons[text].grid_forget()
        del self.del_buttons[text]
        self.labels[text].grid_forget()
        del self.labels[text]
        del self.tasks[text]

    def submitText(self):
        text = self.entry.get()
        self.tasks.update({text: text})
        self.labels.update({text: ctk.CTkLabel(self.scrollable_frame,  text=text,
                                               fg_color="transparent", anchor="w", width=200)})
        self.del_buttons.update({text: ctk.CTkButton(self.scrollable_frame, text="delete",
                                                     command=lambda: self.delete(text), width=10)})

        for key, x in enumerate(self.tasks):
            self.del_buttons[x].grid(column=1, row=key, sticky="e",
                                     padx=(10, 0), pady=(0, 10))
            self.labels[x].grid(column=1, row=key, sticky="e",
                                padx=(10, 0), pady=(0, 10))


toDoList()
