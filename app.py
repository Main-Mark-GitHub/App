import customtkinter as ctk
from config import *
from methods import get


ctk.set_appearance_mode("dark")  # set dark theme 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(TITLE)
        self.geometry(GEOMETRY)

        self.frames = {}
        for F in (StartPage, DetailPage):
            page_name = F.__name__
            frame = F(parent=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show_frame(self, page_name, value=None):
        frame = self.frames[page_name]
        frame.tkraise()
        if value is not None and isinstance(frame, DetailPage):
            frame.update_label(value) 

class StartPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        for el in CRYPTOCURRENCY:
            button = ctk.CTkButton(self, text=el, command=lambda el=el: parent.show_frame("DetailPage", get(el)))
            button.pack(fill='x', padx=10, pady=5)

class DetailPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        button = ctk.CTkButton(self, text="<--", command=lambda: parent.show_frame("StartPage"))
        button.pack(pady=10)

        self.label = ctk.CTkLabel(self, text="", font=FONT)
        self.label.pack(expand=True, fill='both', padx=10, pady=10)

    def update_label(self, value):
        self.value = value
        self.label.configure(text=f"{self.value['Name']}\n{self.value['Price']}\n{self.value['High']}\n{self.value['Low']}")
        self.timer()

    def timer(self):
        current_info = get(self.value["Name"])  
        self.label.configure(text=f"{current_info['Name']}\n{current_info['Price']}\n{current_info['High']}\n{current_info['Low']}")  
        self.after(TIME_TO_SLEEP, self.timer)

if __name__ == "__main__":
    app = App()
    app.mainloop()
