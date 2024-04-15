# file cơ bản
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("600x600")
window.title("Tic-tac-toe")
window.config(bg= "#cc9900")

def check_rows():
    for i in range(0, 9, 3):
        if button_list[i]["text"] == button_list[i+1]["text"] and button_list[i+1]["text"] == button_list[i+2]["text"]:
            return button_list[i]["text"]

def check_cols():
    for i in range(0, 3):
        if button_list[i]["text"] == button_list[i+3]["text"] and button_list[i+3]["text"] == button_list[i+6]["text"]:
            return button_list[i]["text"]

def check_diag():
    diag = [0, 4, 8, 2, 4, 6]
    for i in range(0, 4, 3):
        if button_list[diag[i]]["text"] == button_list[diag[i + 1]]["text"] == button_list[diag[i + 2]]["text"]:
            return button_list[diag[i]]["text"]

def check_tie():
    for button in button_list:
        if button["text"] != "X" and button["text"] != "O":
            return False
    return True

def check_win():
    choose = ''
    player_win = check_rows()
    if player_win != None:
        choose = messagebox.askyesno("Message", player_win + " win. Do you want to play again?")
    else:
        player_win = check_cols()
        if player_win != None:
            choose = messagebox.askyesno("Message", player_win + " win. Do you want to play again?")
        else:
            player_win = check_diag()
            if player_win != None:
                choose = messagebox.askyesno("Message", player_win + " win. Do you want to play again?")
            elif check_tie() == True:
                player_win = "-"  
                choose = messagebox.askyesno("Message", "It's a tie! Do you want to play again?")

    global scoreX, scoreO
    if choose == False: 
        window.destroy()
    elif choose == True:  
        if player_win == "X":
            scoreX = scoreX + 10
            scoreO = scoreO - 5
        elif player_win == "O":
            scoreX = scoreX - 5
            scoreO = scoreO + 10
        elif player_win == "-":
            scoreX = scoreX + 5
            scoreO = scoreO + 5
        reset()
        return True
    return False

def reset():
    i = 1
    for button in button_list:
        button.config(text= "Button_"+str(i), bg= "white", fg= "blue", state= "active")
        i = i+1
    global turn, priority
    score_labelX.config(text=name_playerX + ": " + str(scoreX))
    score_labelO.config(text=name_playerO + ": " + str(scoreO))
    turn = 1
    priority = [button_5, button_1, button_3, button_7, button_9, button_2, button_4, button_6, button_8]

def check_almost_win_rows():
    for i in range(0, 9, 3):
        if button_list[i]["text"] == button_list[i+1]["text"] and button_list[i+2]["text"] not in symbol:
            return button_list[i+2]
        if button_list[i+1]["text"] == button_list[i+2]["text"] and button_list[i]["text"] not in symbol:
            return button_list[i]
        if button_list[i]["text"] == button_list[i+2]["text"] and button_list[i+1]["text"] not in symbol:
            return button_list[i+1]

def check_almost_win_cols():
    for i in range(0, 3):
        if button_list[i]["text"] == button_list[i + 3]["text"] and button_list[i + 6]["text"] not in symbol:
            return button_list[i + 6]
        if button_list[i + 3]["text"] == button_list[i + 6]["text"] and button_list[i]["text"] not in symbol:
            return button_list[i]
        if button_list[i]["text"] == button_list[i + 6]["text"] and button_list[i + 3]["text"] not in symbol:
            return button_list[i + 3]

def check_almost_win_diags():
    diag = [0, 4, 8, 2, 4, 6]
    for i in range(0, 4, 3):
        if button_list[diag[i]]["text"] == button_list[diag[i + 1]]["text"] and button_list[diag[i + 2]]["text"] not in symbol:
            return button_list[diag[i + 2]]
        if button_list[diag[i + 1]]["text"] == button_list[diag[i + 2]]["text"] and button_list[diag[i]]["text"] not in symbol:
            return button_list[diag[i]]
        if button_list[diag[i]]["text"] == button_list[diag[i + 2]]["text"] and button_list[diag[i + 1]]["text"] not in symbol:
            return button_list[diag[i + 1]]

def CPU():
    global turn, priority
    if turn == 1: 
        priority[0].config(text="O", bg="white", state="disable")
        priority.pop(0)
    else: 
        almost_win = check_almost_win_rows()
        if almost_win != None:
            almost_win.config(text="O", bg="white", state="disable")
            priority.remove(almost_win)
        else:
            almost_win = check_almost_win_cols()
            if almost_win != None:
                almost_win.config(text="O", bg="white", state="disable")
                priority.remove(almost_win)
            else:
                almost_win = check_almost_win_diags()
                if almost_win != None:
                    almost_win.config(text="O", bg="white", state="disable")
                    priority.remove(almost_win)
                else: 
                    priority[0].config(text="O", bg="white", state="disable")
                    priority.pop(0)

label = tk.Label(window, text = "Welcome to Tic-tac-toe!", font=("Arial Bold", 30))
label.place(x=75, y=0)

button_size = 150
turn = 1
mode = 1 
scoreX = 0 
scoreO = 0 
symbol = ["X", "O"]

def button1_click():
    global turn
    if mode == 2: 
        if turn % 2 == 0:
            button_1.config(text="O", bg="white", state="disable")
        else:
            button_1.config(text="X", bg="white", state="disable")
    else:
        button_1.config(text="X", bg="white", state="disable")
        priority.remove(button_1)
        if check_win() == True:
            return
        CPU()
        print("Turn", turn, ": ", priority)
    if check_win() == True:
        return
    turn = turn + 1
def button2_click():
    global turn
    if mode == 2:
        if turn % 2 == 0:
            button_2.config(text="O", bg="white", state="disable")
        else:
            button_2.config(text="X", bg="white", state="disable")
    else:
        button_2.config(text="X", bg="white", state="disable")
        priority.remove(button_2)
        if check_win() == True:
            return
        CPU()
        print("Turn", turn, ": ", priority)
    if check_win() == True:
        return
    turn = turn + 1
def button3_click():
    global turn
    if mode == 2:
        if turn % 2 == 0:
            button_3.config(text="O", bg="white", state="disable")
        else:
            button_3.config(text="X", bg="white", state="disable")
    else:
        button_3.config(text="X", bg="white", state="disable")
        priority.remove(button_3)
        if check_win() == True:
            return
        CPU()
        print("Turn", turn, ": ", priority)
    if check_win() == True:
        return
    turn = turn + 1
def button4_click():
    global turn
    if mode == 2:
        if turn % 2 == 0:
            button_4.config(text="O", bg="white", state="disable")
        else:
            button_4.config(text="X", bg="white", state="disable")
    else:
        button_4.config(text="X", bg="white", state="disable")
        priority.remove(button_4)
        if check_win() == True:
            return
        CPU()
        print("Turn", turn, ": ", priority)
    if check_win() == True:
        return
    turn = turn + 1
def button5_click():
    global turn
    if mode == 2:
        if turn % 2 == 0:
            button_5.config(text="O", bg="white", state="disable")
        else:
            button_5.config(text="X", bg="white", state="disable")
    else:
        button_5.config(text="X", bg="white", state="disable")
        priority.remove(button_5)
        if check_win() == True:
            return
        CPU()
        print("Turn", turn, ": ", priority)
    if check_win() == True:
        return
    turn = turn + 1
def button6_click():
    global turn
    if mode == 2:
        if turn % 2 == 0:
            button_6.config(text="O", bg="white", state="disable")
        else:
            button_6.config(text="X", bg="white", state="disable")
    else:
        button_6.config(text="X", bg="white", state="disable")
        priority.remove(button_6)
        if check_win() == True:
            return
        CPU()
        print("Turn", turn, ": ", priority)
    if check_win() == True:
        return
    turn = turn + 1
def button7_click():
    global turn
    if mode == 2:
        if turn % 2 == 0:
            button_7.config(text="O", bg="white", state="disable")
        else:
            button_7.config(text="X", bg="white", state="disable")
    else:
        button_7.config(text="X", bg="white", state="disable")
        priority.remove(button_7)
        if check_win() == True:
            return
        CPU()
        print("Turn", turn, ": ", priority)
    if check_win() == True:
        return
    turn = turn + 1
def button8_click():
    global turn
    if mode == 2:
        if turn % 2 == 0:
            button_8.config(text="O", bg="white", state="disable")
        else:
            button_8.config(text="X", bg="white", state="disable")
    else:
        button_8.config(text="X", bg="white", state="disable")
        priority.remove(button_8)
        if check_win() == True:
            return
        CPU()
        print("Turn", turn, ": ", priority)
    if check_win() == True:
        return
    turn = turn + 1
def button9_click():
    global turn
    if mode == 2:
        if turn % 2 == 0:
            button_9.config(text="O", bg="white", state="disable")
        else:
            button_9.config(text="X", bg="white", state="disable")
    else:
        button_9.config(text="X", bg="white", state="disable")
        priority.remove(button_9)
        if check_win() == True:
            return
        CPU()
        print("Turn", turn, ": ", priority)
    if check_win() == True:
        return
    turn = turn + 1

def click_button_ok():
    global score_labelX, score_labelO, name_playerX, name_playerO
   
    name_label1.place_forget()
    name_entry1.place_forget()
    button_ok.place_forget()

    name_playerX = name_entry1.get().upper()
    if mode == 1:
        name_playerO = "COMPUTER" 
    else:
        name_playerO = name_entry2.get().upper()
        name_label2.place_forget()
        name_entry2.place_forget()

    score_labelX = tk.Label(window, text=name_playerX + ": 0", font=("Arial Bold", 18))
    score_labelX.place(x=120, y=70)
    score_labelO = tk.Label(window, text=name_playerO + ": 0", font=("Arial Bold", 18))
    score_labelO.place(x=340, y=70)

    button_1.place(x=75, y=120, width=button_size, height=button_size)
    button_2.place(x=75 + button_size, y=120, width=button_size, height=button_size)
    button_3.place(x=75 + button_size * 2, y=120, width=button_size, height=button_size)
    button_4.place(x=75, y=120 + button_size, width=button_size, height=button_size)
    button_5.place(x=75 + button_size, y=120 + button_size, width=button_size, height=button_size)
    button_6.place(x=75 + button_size * 2, y=120 + button_size, width=button_size, height=button_size)
    button_7.place(x=75, y=120 + button_size * 2, width=button_size, height=button_size)
    button_8.place(x=75 + button_size, y=120 + button_size * 2, width=button_size, height=button_size)
    button_9.place(x=75 + button_size * 2, y=120 + button_size * 2, width=button_size, height=button_size)

def click_one_player_mode():
    mode_label.place_forget()
    one_player_mode.place_forget()
    two_player_mode.place_forget()
    global name_label1, name_entry1, button_ok, mode 
    mode = 1

    name_label1 = tk.Label(window, text="Enter your name: ", font=("Calibri", 15), bg="#cc9900")
    name_label1.place(x=100, y=150)

    name_entry1 = tk.Entry(window, font=("Arial", 10), justify='center')
    name_entry1.place(x=260, y=150, width=150, height=30)

    button_ok = tk.Button(text="OK", command=click_button_ok)
    button_ok.place(x=420, y=150, width=50, height=30)

def click_two_player_mode():
    mode_label.place_forget()
    one_player_mode.place_forget()
    two_player_mode.place_forget()
    global name_label1, name_label2, name_entry1, name_entry2, button_ok, mode 
    mode = 2

    name_label1 = tk.Label(window, text="Enter player1's name: ", font=("Calibri", 15), bg="#cc9900")
    name_label1.place(x=100, y=90)
    name_label2 = tk.Label(window, text="Enter player2's name: ", font=("Calibri", 15), bg="#cc9900")
    name_label2.place(x=100, y=150)

    name_entry1 = tk.Entry(window, font=("Arial", 10), justify='center')
    name_entry1.place(x=300, y=90, width=150, height=30)
    name_entry2 = tk.Entry(window, font=("Arial", 10), justify='center')
    name_entry2.place(x=300, y=150, width=150, height=30)

    button_ok = tk.Button(text="OK", command=click_button_ok)
    button_ok.place(x=280, y=210, width=50, height=30)

mode_label = tk.Label(window, text= "Choose mode:", bg= "#cc9900", font=("Calibri Bold", 20))
mode_label.place(x= 200, y= 70)
one_player_mode = tk.Checkbutton(window, text= "One Player Mode", bg= "#cc9900", font=("Calibri", 15), command= click_one_player_mode)
one_player_mode.place(x= 220, y= 120)
two_player_mode = tk.Checkbutton(window, text= "Two Player Mode", bg= "#cc9900", font=("Calibri", 15), command= click_two_player_mode)
two_player_mode.place(x= 220, y= 160)



button_1 = tk.Button(text="Button 1", bg= "blue", activebackground= "white", fg= "white", activeforeground= "blue", command= button1_click)
button_2 = tk.Button(text="Button 2", bg= "blue", activebackground= "white", fg= "white", activeforeground= "blue", command= button2_click)
button_3 = tk.Button(text="Button 3", bg= "blue", activebackground= "white", fg= "white", activeforeground= "blue", command= button3_click)
button_4 = tk.Button(text="Button 4", bg= "blue", activebackground= "white", fg= "white", activeforeground= "blue", command= button4_click)
button_5 = tk.Button(text="Button 5", bg= "blue", activebackground= "white", fg= "white", activeforeground= "blue", command= button5_click)
button_6 = tk.Button(text="Button 6", bg= "blue", activebackground= "white", fg= "white", activeforeground= "blue", command= button6_click)
button_7 = tk.Button(text="Button 7", bg= "blue", activebackground= "white", fg= "white", activeforeground= "blue", command= button7_click)
button_8 = tk.Button(text="Button 8", bg= "blue", activebackground= "white", fg= "white", activeforeground= "blue", command= button8_click)
button_9 = tk.Button(text="Button 9", bg= "blue", activebackground= "white", fg= "white", activeforeground= "blue", command= button9_click)

button_list = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
priority = [button_5, button_1, button_3, button_7, button_9, button_2, button_4, button_6, button_8]

window.mainloop()