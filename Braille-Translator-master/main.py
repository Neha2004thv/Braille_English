import tkinter as tk
from tkinter import filedialog, messagebox
import alphaToBraille
import brailleToAlpha
import printer

def translate_text_to_braille():
    text_input = text_entry.get("1.0", "end-1c")  # Retrieve text from the text entry field
    braille_output.delete("1.0", "end")  # Clear previous output
    braille_output.insert("end", alphaToBraille.translate(text_input))  # Translate text to Braille and display

def translate_braille_to_text():
    braille_input = braille_entry.get("1.0", "end-1c")  # Retrieve text from the Braille entry field
    text_output.delete("1.0", "end")  # Clear previous output
    text_output.insert("end", brailleToAlpha.translate(braille_input))  # Translate Braille to text and display

def open_file_and_translate():
    file_path = filedialog.askopenfilename()  # Open file dialog to select a file
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                translated_content = alphaToBraille.translate(content)
                text_output.delete("1.0", "end")  # Clear previous output
                text_output.insert("end", translated_content)  # Display translated content
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")

def show_translation_map():
    translation_map = printer.all_braille()
    messagebox.showinfo("Braille Translation Map", translation_map)

# Create the main application window
root = tk.Tk()
root.title("Braille Translator")

# Create and place widgets for text to Braille translation
text_entry_label = tk.Label(root, text="Enter text to translate to Braille:")
text_entry_label.grid(row=0, column=0, padx=5, pady=5)

text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=1, column=0, padx=5, pady=5)

translate_text_button = tk.Button(root, text="Translate to Braille", command=translate_text_to_braille)
translate_text_button.grid(row=2, column=0, padx=5, pady=5)

braille_output_label = tk.Label(root, text="Braille Output:")
braille_output_label.grid(row=3, column=0, padx=5, pady=5)

braille_output = tk.Text(root, height=5, width=50)
braille_output.grid(row=4, column=0, padx=5, pady=5)

# Create and place widgets for Braille to text translation
braille_entry_label = tk.Label(root, text="Enter Braille to translate to text:")
braille_entry_label.grid(row=0, column=1, padx=5, pady=5)

braille_entry = tk.Text(root, height=5, width=50)
braille_entry.grid(row=1, column=1, padx=5, pady=5)

translate_braille_button = tk.Button(root, text="Translate to Text", command=translate_braille_to_text)
translate_braille_button.grid(row=2, column=1, padx=5, pady=5)

text_output_label = tk.Label(root, text="Text Output:")
text_output_label.grid(row=3, column=1, padx=5, pady=5)

text_output = tk.Text(root, height=5, width=50)
text_output.grid(row=4, column=1, padx=5, pady=5)

# Create and place additional widgets
open_file_button = tk.Button(root, text="Open File and Translate", command=open_file_and_translate)
open_file_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

show_map_button = tk.Button(root, text="Show Braille Translation Map", command=show_translation_map)
show_map_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
