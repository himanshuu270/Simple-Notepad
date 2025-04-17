
import tkinter as tk  # Import tkinter module for creating GUI applications
from tkinter import *  # Import all classes and constants from tkinter
import tkinter.messagebox as tm  # Import messagebox for showing pop-ups
from tkinter import ttk  # Import tkinter's themed widgets
from tkinter.filedialog import askopenfilename, asksaveasfilename  # Import file dialog for opening/saving files
import os  # Import os module for file handling operations

# Create the main window for the application
root = tk.Tk()
root.title("tkinter project")  # Set the title of the window
root.geometry("650x325")  # Set the dimensions of the window
root.iconbitmap("gui.ico")  # Set the window icon

# Add a vertical scrollbar to the text area
scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)  # Place the scrollbar on the right side

# Add a text area with scroll functionality
text = Text(root, yscrollcommand=scrollbar.set, font="consolas 12")
text.pack(expand=True, fill="both")  # Expand text area to fill available space
scrollbar.config(command=text.yview)  # Link the scrollbar to the text area

file = None

# Function to save the contents of the text area to a file
def save_file():
    global file
    if file is None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                 filetypes=[("All files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + "- Notepad")
            tm.showinfo("Info", "Your info is saved")  # Show confirmation message
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()
        tm.showinfo("Info", "Your info is saved")  # Show confirmation message

# Function to change the background color of the text area
def change_bg_color():
    def set_color():  # Nested function to apply selected color
        color = color_var.get()  # Get the selected color from the variable
        text.config(bg=color)  # Change the background color of the text area

    # Create a new window for color selection
    color_window = Toplevel(root)
    color_window.title("Select Background Color")  # Set title for the color selection window
    color_window.geometry("200x150")  # Set dimensions for the window

    # Variable to store selected color
    color_var = StringVar(value="Light Blue")
    # List of available colors
    colors = ["Light Blue", "Light Yellow", "Light Green", "Pink"]

    # Create radio buttons for each color
    for c in colors:
        Radiobutton(color_window, text=c, value=c, variable=color_var, command=set_color).pack(anchor=W)

# Functions for editing operations in the text area
def cut():
    text.event_generate("<<Cut>>")  # Generate 'cut' event

def copy():
    text.event_generate("<<Copy>>")  # Generate 'copy' event

def paste():
    text.event_generate("<<Paste>>")  # Generate 'paste' event

# Function to create a new file by clearing the text area
def new_file():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)

# Function to open a file and display its content in the text area
def open_file():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

# Function to show the 'About' information
def about():
    tm.showinfo("About", "This is a notepad created by Himanshu")  # Show 'About' info in a messagebox

# Function to show contact information
def contact():
    tm.showinfo("Contact", "Contact us at himanshu00@gmail.com")  # Show contact info in a messagebox

# Create a menu bar for the application
menubar = Menu(root, tearoff=0)

# File Menu for file-related operations
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)  # Add 'New' menu item
file_menu.add_command(label="Open", command=open_file)  # Add 'Open' menu item
file_menu.add_command(label="Save", command=save_file)  # Add 'Save' menu item
menubar.add_cascade(label="File", menu=file_menu)  # Add 'File' menu to the menu bar
file_menu.add_separator()  # Add a separator line
file_menu.add_command(label="Exit", command=root.quit)  # Add 'Exit' menu item to close the application

# Edit Menu for editing operations
edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)  # Add 'Cut' menu item
edit_menu.add_command(label="Copy", command=copy)  # Add 'Copy' menu item
edit_menu.add_command(label="Paste", command=paste)  # Add 'Paste' menu item
edit_menu.add_command(label="Change Background colour", command=change_bg_color)  # Add background color change menu item
menubar.add_cascade(label="Edit", menu=edit_menu)  # Add 'Edit' menu to the menu bar
root.config(menu=menubar)  # Apply the menu bar to the root window

# Help Menu for information and reporting issues
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=about)  # Add 'About' menu item
help_menu.add_command(label="Report issues", command=contact)  # Add 'Report issues' menu item
menubar.add_cascade(label="Help", menu=help_menu)  # Add 'Help' menu to the menu bar
root.config(menu=menubar)  # Apply the menu bar to the root window

# Start the Tkinter event loop
root.mainloop()