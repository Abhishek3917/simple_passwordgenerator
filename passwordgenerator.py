# password generator
import turtle
import random
import pyperclip

screen=turtle.Screen()
screen.bgcolor("grey")
screen.title("Password Generator")

def pass_gen():
    alpabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

    symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    digit=['1','2','3','4','5','6','7','8','9','0']

    input_alpha=int(screen.numinput("Enter Value","Enter the number of alphabet needed"))
    input_sym=int(screen.numinput("Enter Value","Enter the number of symbol needed"))
    input_digits=int(screen.numinput("Enter Value","Enter the number of digit needed"))
    password_list=[]
    for i in range(0,input_alpha):
        password_list.append(random.choice(alpabets))
    for i in range(0,input_sym):
        password_list.append(random.choice(symbols))
    for i in range(0,input_digits):
        password_list.append(random.choice(digit))

    random.shuffle(password_list)

    password=""
    for i in password_list:
        password+=i
    
    menu.clear()
    menu.goto(-300,100)
    menu.write(password, font=("Arial", 30))
    pyperclip.copy(password)
    menu.goto(-200,30)
    menu.write("password is copied to clipboard", font=("Arial", 20))


menu=turtle.Turtle()
menu.hideturtle()
menu.penup()
menu.goto(-300,100)
menu.write("1. Add Account", font=("Arial", 16))
menu.goto(-300,50)
menu.write("2. Exit", font=("Arial", 16))
screen.onkey(pass_gen, "1")
screen.onkey(exit,"2")

screen.listen()
turtle.mainloop()
