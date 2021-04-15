import tkinter as tk
import wikipediaapi
from functools import partial


def display_essay(text):
    frame = tk.Frame()
    text_box = tk.Text(master=frame)
    text_box.insert('1.0', text)

    frame.pack(fill=tk.BOTH)
    text_box.pack(fill=tk.BOTH)

    tk.mainloop()


def create_start_page():
    def generate_essay():
        topic = entry.get()
        frame.destroy()
        page = wiki_wiki.page(topic)
        text = page.text
        display_essay(text)
    frame = tk.Frame()


    label = tk.Label(master=frame, text='Welcome to Essay Generator. Please enter the topic of the essay you would like me to generate:')
    entry = tk.Entry(master=frame)
    button = tk.Button(master=frame, text='Generate', command=generate_essay)

    frame.pack(fill=tk.BOTH)
    label.pack(fill=tk.BOTH)
    entry.pack(fill=tk.BOTH)
    button.pack(fill=tk.BOTH)

    tk.mainloop()


wiki_wiki = wikipediaapi.Wikipedia('en')
window = tk.Tk()
window.geometry("600x300")
window.title('Essay Generator')

create_start_page()
