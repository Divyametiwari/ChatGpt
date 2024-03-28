from tkinter import *

root = Tk()

def send_message():
    message = "Divya: " + e.get()
    text.insert(END, "\n" + message)
    if e.get() == 'hii':
        text.insert(END, "\n" + "Raunak: hello")
    elif e.get() == 'hello':
        text.insert(END, "\n" + "Raunak: hi")
    elif e.get() == 'How are you?':
        text.insert(END, "\n" + "Raunak: I'm fine")
    elif e.get() == "How's your study going on?":
        text.insert(END, "\n" + "Raunak: It's good")
    else:
        text.insert(END, "\n" + "Raunak: Sorry, I found many difficulties to cover syllabus")

text = Text(root, bg='red', fg='white')
text.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=80)
e.grid(row=1, column=0)

send_button = Button(root, text='Send', bg='deeppink', fg='white', width=20, command=send_message)
send_button.grid(row=1, column=1)

root.title('Raunak Divya')
root.mainloop()