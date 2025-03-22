from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

root = Tk()
root.title("Google Translate")
root.geometry("1080x400")
root.configure(bg="white")

# Supported languages
languages = GoogleTranslator().get_supported_languages()
language_dict = {lang.title(): lang for lang in languages}

def label_change():
    """Update labels dynamically based on selected languages."""
    label1.config(text=combo1.get())
    label2.config(text=combo2.get())
    root.after(1000, label_change)

def translate_now():
    """Translate text from source to target language."""
    try:
        text_ = text1.get(1.0, END).strip()
        if text_:
            source_lang = language_dict.get(combo1.get().title())
            target_lang = language_dict.get(combo2.get().title())
            
            if not source_lang or not target_lang:
                messagebox.showerror("Error", "Invalid language selection")
                return
            
            translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text_)
            text2.delete(1.0, END)
            text2.insert(END, translated_text)
        else:
            messagebox.showerror("Error", "Please enter text to translate.")
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")

# Language selection dropdowns
combo1 = ttk.Combobox(root, values=list(language_dict.keys()), font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("English")

combo2 = ttk.Combobox(root, values=list(language_dict.keys()), font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("Select Language")

# Labels
label1 = Label(root, text="English", font="Segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)
label2 = Label(root, text="English", font="Segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# Text Input
f = Frame(root, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)
text1 = Text(f, font="Roboto 20", bg="White", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f, command=text1.yview)
scrollbar1.pack(side="right", fill="y")
text1.configure(yscrollcommand=scrollbar1.set)

# Text Output
f1 = Frame(root, bg="black", bd=5)
f1.place(x=620, y=118, width=440, height=210)
text2 = Text(f1, font="Roboto 20", bg="White", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1, command=text2.yview)
scrollbar2.pack(side="right", fill="y")
text2.configure(yscrollcommand=scrollbar2.set)

# Translate Button
translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2",
                   bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=480, y=250)

# Start updating labels
label_change()

# Run application
root.mainloop()
