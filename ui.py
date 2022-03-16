from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 150, width= 280, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.logo_img = PhotoImage(file="true.png")
        self.logo_img2 = PhotoImage(file="false.png")

        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("arial", 12))
        self.score_text.grid(column=1, row=0, pady=20)

        self.check_button = Button(image=self.logo_img, background=THEME_COLOR, highlightthickness=0, borderwidth=0
                                   , command=self.true_pressed)
        self.check_button.grid(column=0, row=2, pady=30)

        self.x_button = Button(image=self.logo_img2, background=THEME_COLOR, highlightthickness=0, borderwidth=0,
                               command= self.false_pressed)
        self.x_button.grid(column=1, row=2, pady=30)


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right: #if True/False matches the wuestion answer then change background color
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)