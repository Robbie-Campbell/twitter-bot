from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
from bot.bot_logic import Bot
from bot.twitter_navigation import LoginPath


class MakeTweet:
    def __init__(self):
        root = Tk()
        arial16 = Font(family="arial", size=16, weight="bold")
        root.title("Twitter Bot Service")
        root.configure(background="#115")
        root.resizable(False, False)
        title = Label(root, bg="#115", fg="#DDD", font=arial16, text="Post a Bot Botmanson tweet")
        title.grid(row=0, column=0, columnspan=2)
        canvas = Canvas(root, width=360, height=339, bd=0, highlightthickness=0)
        canvas.grid(row=1, column=0)
        img = ImageTk.PhotoImage(Image.open("bot/botbotmanson.JPG"))
        canvas.create_image(0, 0, anchor=NW, image=img)
        button = Button(text="Post New Tweet", font=arial16, bg="#1DA1F2", command=self.post_tweet)
        button.grid(row=1, column=1, sticky="news", ipadx=50)
        root.mainloop()

    def post_tweet(self):
        LoginPath(Bot().generate_a_post()).make_post()


if __name__ == "__main__":
    MakeTweet()