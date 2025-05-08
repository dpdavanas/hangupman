import tkinter as tk
from tkinter import messagebox
import random

#sarkasts ar vārdiem ko var uzminēt
words = ['python', 'programming', 'computer', 'algorithm', 'function', 'variable', 'syntax']

word_to_guess =random.choice(words)
guessed_letters = []
attempts = 6

#uztaisīt logu
window = tk.Tk()
window.title("Karātavas")

#funkcija, lai apskatītos vai spele ir beigusies
def is_game_over():
    return check_win() or check_loss()

#funkcija, lai apskatītos vai spēlētaijs ir vinnējis
def check_win():
    return all(letter in guessed_letters for letter in word_to_guess)

#funkcija, lai apskatītos vai spēlētaijs ir zaudējis
def check_loss():
    return attempts ==0

#funkcija, lai uzminētu burtu
def guess_letter():
    global attempts
    letter = letter_entry.get().lower()
    if letter.isalpha() and len(letter) ==1:
        if letter in guessed_letters:
            messagebox.showinfo("karātavas", f"Jūs jau esat minējuši burtu '{letter}'")
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            update_word_display()
            if check_win():
                messagebox.showinfo("Karātavas", f"Apsveicu! Jūs vinnējāt!")
                reset_game()
        else:
            guessed_letters.append(letter)
            attempts -= 1
            update_attempts_display()
            draw_hangman()
            if check_loss():
                messagebox.showinfo("Karātavas", f"Tu zaudēji! vārds bija:" + word_to_guess)
                reset_game()
        letter_entry.delete(0, tk.END)  #atbrīvo burtu ievadīsanas laukumu
    else:
        messagebox.showinfo("Karātvas", "Lūdzu ievadiet vienu burtu.")

#Funkcija, lai restartētu spēli
def reset_game():
    global word_to_guess, guessed_letters, attempts
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6
    update_word_display()
    update_attempts_display()
    draw_hangman()

#Funkcija, lai atjaunotu vārdu displeju
def update_word_display():
    display_word = ""
    for  letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
        display_word += " "
        word_label.config(text=display_word)

#Funkcija, lai atjaunotu mēģinājumu displeju
def update_attempts_display():
    attempts_label.config(text=f"Mēģinājumi atlikuši: {attempts}")

#Funkcija, lai uzzīmētu karātāju
def draw_hangman():
    canvas.delete("Karātaijs")
    if attempts <6:
        canvas.create_oval(125, 125, 175, 175, width=4, tags="Karātaijs") #galva
    if attempts <5:
        canvas.create_line(150, 175, 150, 225, width=4, tags="Karātaijs") #ķermenis
    if attempts <4:
        canvas.create_line(150, 200, 125, 175, width=4, tags="Karātaijs") #kreisā roka
    if attempts <3:
        canvas.create_line(150, 200, 175, 175, width=4, tags="Karātaijs") #labā roka
    if attempts <2:
        canvas.create_line(150, 225, 125, 250, width=4, tags="Karātaijs") #kreisā kāja
    if attempts <1:
        canvas.create_line(150, 225, 175, 250, width=4, tags="Karātaijs") #labā kāja

#Izvediot GUI elementus
word_label = tk.Label(window, text="", font=("Arial",24))
attempts_label = tk.Label(window, text="", font=("Arial", 16))
letter_entry = tk.Entry(window, width=5, font=("Arial", 16))
guess_button = tk.Button(window, text="Minēt", command=guess_letter)
reset_button = tk.Button(window, text="Restartēt", command=reset_game)
canvas = tk.Canvas(window, width=300, height=300)
canvas.create_line(50, 250, 250, 250, width=4) 
canvas.create_line(200, 250, 200, 100, width=4)
canvas.create_line(100,100,200,100, width=4)
canvas.create_line(150,100, 150, 120, width=4)
canvas.pack()

#apkopot GUI elementus
word_label.pack()
attempts_label.pack()
letter_entry.pack()
guess_button.pack()
reset_button.pack()

#Atjaunot sākotnējo displeju
update_word_display()
update_attempts_display()
draw_hangman()

#palaist spēli
window.mainloop()