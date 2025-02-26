import customtkinter as ctk
from customtkinter import filedialog 

# Initialize customtkinter
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter Modal Window Example")
        self.geometry("780x520")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        combobox = ctk.CTkComboBox(master=self,
                                     values=["option 1", "option 2"],
                                     command=self.on_closing)
        combobox.pack(padx=20, pady=10)

        # Main window button to open the modal
        open_modal_button = ctk.CTkButton(self, text="Open FOLDER SELECT FILE", command=self.selectfile)
        open_modal_button.pack(pady=20)

    def open_modal(self):
        # Create a modal window
        modal = ctk.CTkToplevel(self)
        modal.title("Modal Window")
        modal.geometry("300x200")
        modal.grab_set()  # Make the window modal
        modal.transient(self)  # Link the modal to the main window

        label = ctk.CTkLabel(modal, text="This is a modal window.")
        label.pack(pady=20)

        close_button = ctk.CTkButton(modal, text="Close", command=modal.destroy)
        close_button.pack(pady=10)

        # Prevent resizing (optional)
        modal.resizable(False, False)

    
    def on_closing(self, event=0):
        # res = messagebox.askquestion('Confirm', 'Are you sure?')
        # if res == 'yes':
        self.destroy()

    def selectfile(self, event=0):
        filename = filedialog.askopenfilename()
        print(filename)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
