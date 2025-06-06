# Final Python Quiz Game Project

import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random
import time

# --------------------------- QUIZ DATA --------------------------- #
data = {
    'Question': [
        "What is the capital of India?",
        "Which language is used for web apps?",
        "What is 5 + 7?",
        "Which keyword is used to define a function in Python?",
        "What is the output of: 3*7?"
    ],
    'Option1': ["Paris", "Python", "11", "def", "777"],
    'Option2': ["London", "Java", "12", "func", "21"],
    'Option3': ["New Delhi", "C++", "10", "define", "37"],
    'Option4': ["Chennai", "HTML", "13", "lambda", "111"],
    'Answer': ["New Delhi", "HTML", "12", "def", "21"]
}

questions_df = pd.DataFrame(data)
questions_df = questions_df.sample(frac=1).reset_index(drop=True)  # Shuffle

# --------------------------- VARIABLES --------------------------- #
current_question = 0
score = 0
total_questions = len(questions_df)

# --------------------------- TIMER FEATURE --------------------------- #
TIMER_DURATION = 15  # seconds
countdown_job = None

# --------------------------- FUNCTIONS --------------------------- #
def check_answer(selected_option):
    global current_question, score
    correct = questions_df.iloc[current_question]['Answer']
    if selected_option == correct:
        score += 1
    current_question += 1
    next_question()

def next_question():
    global countdown_job
    if countdown_job:
        window.after_cancel(countdown_job)

    if current_question < total_questions:
        q = questions_df.iloc[current_question]
        question_label.config(text=f"Q{current_question+1}: {q['Question']}")
        var1.set(q['Option1'])
        var2.set(q['Option2'])
        var3.set(q['Option3'])
        var4.set(q['Option4'])
        start_timer(TIMER_DURATION)
    else:
        show_result()

def show_result():
    messagebox.showinfo("Quiz Completed", f"Your Score: {score}/{total_questions}")
    window.destroy()

def start_timer(count):
    global countdown_job
    timer_label.config(text=f"Time left: {count}s")
    if count > 0:
        countdown_job = window.after(1000, start_timer, count - 1)
    else:
        messagebox.showwarning("Time's up!", "Moving to next question.")
        next_question()

# --------------------------- GUI SETUP --------------------------- #
window = tk.Tk()
window.title("Python Quiz Game")
window.geometry("500x400")
window.configure(bg="lightblue")

question_label = tk.Label(window, text="", font=("Arial", 14), wraplength=450, bg="lightblue")
question_label.pack(pady=20)

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()

btn1 = tk.Button(window, textvariable=var1, width=30, command=lambda: check_answer(var1.get()))
btn2 = tk.Button(window, textvariable=var2, width=30, command=lambda: check_answer(var2.get()))
btn3 = tk.Button(window, textvariable=var3, width=30, command=lambda: check_answer(var3.get()))
btn4 = tk.Button(window, textvariable=var4, width=30, command=lambda: check_answer(var4.get()))

btn1.pack(pady=5)
btn2.pack(pady=5)
btn3.pack(pady=5)
btn4.pack(pady=5)

timer_label = tk.Label(window, text="", font=("Arial", 12), bg="lightblue")
timer_label.pack(pady=10)

# --------------------------- START QUIZ --------------------------- #
next_question()
window.mainloop()
