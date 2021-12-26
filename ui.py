from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.text_area = Canvas(height=250, width=300, bg="white")
        self.text_area.grid(row=1, column=0, columnspan=2, pady=50)

        self.question = self.text_area.create_text(150, 125, text="testing", width=280, font=("arial", 15, "italic"))

        self.true = PhotoImage(file="images/true.png")
        self.right = Button(image=self.true, highlightthickness=0, command=self.check_true)
        self.right.grid(row=2, column=1)

        self.false = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.false, highlightthickness=0, command=self.check_false)
        self.wrong.grid(row=2, column=0)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.text_area.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.text_area.itemconfig(self.question,
                                      text=f"Q{self.quiz.question_number+1}: {self.quiz.next_question()}")
        else:
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
            self.text_area.itemconfig(self.question,
                                      text=f"Final score: {self.quiz.score}/{self.quiz.question_number}")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.text_area.config(bg="green")
        else:
            self.text_area.config(bg="red")
        self.window.after(1000, self.next_question)
