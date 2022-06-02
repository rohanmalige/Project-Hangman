from tkinter import *
from tkinter import messagebox
import random
import time
from DIC import dic,hangman
import sys

#VISUAL REPRESENTATION AND VARIABLE INITIALIZATION
window = Tk()
window.title("Play the Hangman Game!")
window.configure(background="black")
movie=random.choice(list(dic.keys()))
time.sleep(1)
chances=7
messagebox.showinfo("Welcome to the hangman game","""Welcome to the python hangman game!
This is a game where a person will guess the movie name
                            RULES OF THE GAME
You have {} chances to play this game
You have 3 hints. Use them wisely. Using it looses 1 chance""".format(chances))
num=0
count=0
countspace=0
answer= movie
wrong=[]


#FUNCTION DEFINITION
def clicked(alphabet):
    global chances
    global num
    global count
    global hintlab
    global countspace
    global answer
    global label2
    global wrong
    global label3
    if alphabet=='Hints' and num<=2:
        txt=dic[movie][num]
        label2.configure(text=txt)
        num+=1
        chances-=1
        txt=hangman[chances]
        label3.configure(text=txt)
        if num==3:
                messagebox.showinfo("Sorry","You have Exhausted your hints.")
                btn27=Button(window, text="Hint",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'), borderwidth=0, command=lambda: clicked("Hints"),state=DISABLED ).grid(column=5,row=7)
    elif alphabet in answer:
        for j in range(len(movie)):
            if movie[j]==alphabet:
                textboxes[j]=Button(window, text=alphabet ,bg="black", fg="white",width=3,height=1,font=('Helvetica','20')).grid(column=j+1, row=0)
                count+=1
                answer=answer[:answer.find(movie[j])]+answer[answer.find(movie[j])+1:]
                wrong+=[alphabet]
        else:
            if count==(len(movie)-countspace):
                 messagebox.showinfo("Congratulations","You have won the game.")
                 window.destroy()
                 quit()

    elif alphabet not in wrong:
        wrong+=[alphabet]
        chances = chances - 1;
        txt=hangman[chances]
        label3.configure(text=txt)
    if chances<=0:
            messagebox.showinfo("Game Over","The man has been hanged.")
            window.destroy()
            sys.exit()


            


#PRINTING THE EMPTY TEXTBOXES FOR THE MOVIE NAME
textboxes={}
for i in range(len(movie)):
    if movie[i]!=" ":
        textboxes[i] = Button(window, text="",bg="black", fg="white",width=3,height=1,font=('Helvetica','20')).grid(column=i+1, row=0)
    else:
        textboxes[i]=Label(window,text="            ",bg="black", fg="white").grid(column=i+1,row=0)
        countspace+=1
num=0
Label(window,text="""efefefefefef
fefefefefefe
efefefef
""",fg="black",bg="black").grid(column=0,row=10)



#PRINTING THE ALPHABETS        
btn1 = Button(window, text="A",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("A")).grid(column=1, row=2)
btn2 = Button(window, text="B",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("B")).grid(column=2, row=2)
btn3 = Button(window, text="C",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("C")).grid(column=3, row=2)
btn4 = Button(window, text="D",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("D")).grid(column=4, row=2)
btn5 = Button(window, text="E",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("E")).grid(column=5, row=2)
btn6 = Button(window, text="F",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("F")).grid(column=6, row=2)
btn7 = Button(window, text="G",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("G")).grid(column=7, row=2)
btn8 = Button(window, text="H",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("H")).grid(column=8, row=2)
btn9 = Button(window, text="I",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("I")).grid(column=9, row=2)
btn10 = Button(window, text="J",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("J")).grid(column=10, row=2)
btn11= Button(window, text="K",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("K")).grid(column=2, row=3)
btn12 = Button(window, text="L",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("L")).grid(column=3, row=3)
btn13 = Button(window, text="M",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("M")).grid(column=4, row=3)
btn14 = Button(window, text="N",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("N")).grid(column=5, row=3)
btn15= Button(window, text="O",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("O")).grid(column=6, row=3)
btn16 = Button(window, text="P",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("P")).grid(column=7, row=3)
btn17 = Button(window, text="Q",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("Q")).grid(column=8, row=3)
btn18 = Button(window, text="R",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("R")).grid(column=9, row=3)
btn19 = Button(window, text="S",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("S")).grid(column=3, row=4)
btn20 = Button(window, text="T",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("T")).grid(column=4, row=4)
btn21 = Button(window, text="U",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("U")).grid(column=5, row=4)
btn22 = Button(window, text="V",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("V")).grid(column=6, row=4)
btn23 = Button(window, text="W",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("W")).grid(column=7, row=4)
btn24 = Button(window, text="X",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("X")).grid(column=8, row=4)
btn25 = Button(window, text="Y",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("Y")).grid(column=5, row=5)
btn26 = Button(window, text="Z",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),borderwidth=1,command=lambda: clicked("Z")).grid(column=6, row=5)


#VISUAL REPRESENTATION AND SPACING
Label(window,text="""efefefefefef
fefefefefefe
efefefef
""",bg="black", fg="black").grid(column=0,row=6)
Label(window,text="""efefefefefef
fefefefefefe
efefefef
""",bg="black", fg="black").grid(column=0,row=8)
Label(window,text="""efefefefefef
fefefefefefe
""",bg="black", fg="black").grid(column=0,row=10)
label2=Button(window,text="You Have 3 hints remaining",font=('Helvetica','10'),bg="black", fg="white")
label2.place(x=305,y=510)
label3=Label(window,text="""                          
                          |
                          |
                          |
                          |
                          |
                          |
                          |
              ______________
""",fg="white",bg="black")
label3.grid(column=0,row=0)
btn27=Button(window, text="Hint",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'), borderwidth=0, command=lambda: clicked("Hints") ).grid(column=5,row=7)
window.mainloop()
sys.exit()
