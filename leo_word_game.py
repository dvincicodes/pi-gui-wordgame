import time
class WordGame():
    def __init__(self,secret_word = "default", correct_guess = '', incorrect_guess = ''):
        self.secret_word = secret_word
        self.correct_guess = correct_guess
        self.incorrect_guess = incorrect_guess


    ####    
    def getSecret(self):
        return self.secret_word

    ####    
    def getRight(self):
        return self.correct_guess

    ####
    def getWrong(self):
        return self.incorrect_guess

    ###
    def guess(self,letter):
        
        if self.getState() == "won" or self.getState() == 'lost':
            pass
        elif letter in self.correct_guess or letter in self.incorrect_guess:
            pass
        elif letter in self.secret_word:
            self.correct_guess = self.correct_guess + letter
        else:
            self.incorrect_guess = self.incorrect_guess + letter

    def getHint(self):
        xyz = []
        for i,y in enumerate(self.secret_word):
            if self.secret_word[i] in self.correct_guess:
                xyz.append(self.secret_word[i])
            else:
                xyz.append('?')
        hint = ''.join(xyz)

        return hint

    ####
    def getState(self):
        if self.getHint() == self.secret_word:
            time.sleep(1)
            return "won"
        elif len(self.incorrect_guess) > 5:
            return "lost"
        else:
            return "playing"


##################################
##################################
        
from tkinter import *
import tkinter.messagebox

class WordGameGui(Frame):

    def __init__(self,word = "Default", parent = None):
        
        #self.word = word
        self.wordgame = WordGame(word)
        Frame.__init__(self,parent)

        #BUTTONS
        labels = 'ABCEDFGHIJKLMNOPQRSTUVWXYZ'
        for i,label in enumerate(labels):
            def cmd(key = label):
                self.click(key)
            self.bt1 = Button(self,command =cmd,text = label,width = 5, height = 2, fg = 'blue',font = "Verdana 15 bold")
            self.bt1.grid(row = 4+i//6, column = i%6)     
        
        #RIGHT WIDGETS
        self.right_label = Label(self,text = "Right:",fg = 'green', font = "Verdana 15 bold")
        self.right_label.grid(row = 1, column = 0,columnspan = 2)
        
        self.right_entry = Entry(self)
        self.right_entry.grid(row = 1, column = 2, columnspan = 6)

        #WRONG WIDGETS
        self.wrong_label = Label(self,text = "Wrong:", fg = 'red',font = "Verdana 15 bold")
        self.wrong_label.grid(row = 2, column = 0,columnspan = 2)
        
        self.wrong_entry = Entry(self)
        self.wrong_entry.grid(row = 2, column = 2, columnspan = 6)

        #WORD WIDGETS
        self.word_label = Label(self,text = "Word:",fg = 'black',font = "Verdana 15 bold")
        self.word_label.grid(row = 0, column = 0, columnspan = 2)

        self.word_entry = Entry(self)
        self.word_entry.grid(row = 0, column = 2,columnspan = 4)


    def click(self,key):
        #Guess
        self.wordgame.guess(key)

        #GetRight
        self.right_entry.delete(0,END)
        right_answers = self.wordgame.getRight()
        self.right_entry.insert(0,right_answers)
        
        #GetHint
        self.word_entry.delete(0,END)
        hintt = self.wordgame.getHint()
        self.word_entry.insert(0,hintt)

        #GetWrong
        self.wrong_entry.delete(0,END)
        wrong_answers = self.wordgame.getWrong()
        self.wrong_entry.insert(0,wrong_answers)
        #GetState
        if self.wordgame.getState() == 'won':
            tkinter.messagebox.showinfo(title="CONGRATS", message='You Win!')
        elif self.wordgame.getState() == 'lost':
            tkinter.messagebox.showinfo(title="BETTER LUCK NEXT TIME", message='You Lose!')


  ####GameTest###          
#root = Tk() 
#root.title("Leo's WordGame")
#WordGameGui("HELLOWORLD",root).pack()

