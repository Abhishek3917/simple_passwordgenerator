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

    input_str = screen.textinput("Enter Values", "Enter the number of alphabets, symbols, and digits needed separated by commas (e.g. 3,4,5): ")
    input_list = input_str.split(',')

    if len(input_list) >= 1 and input_list[0] != '':
        input_alpha = int(input_list[0])
    else:
        input_alpha = 0

    if len(input_list) >= 2 and input_list[1] != '':
        input_sym = int(input_list[1])
    else:
        input_sym = 0

    if len(input_list) >= 3 and input_list[2] != '':
        input_digits = int(input_list[2])
    else:
        input_digits = 0

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
    copy = screen.numinput("do u need to copy","enter 1 or to regenerate press any key")
    copy=int(copy)
    if(copy==1):
        pyperclip.copy(password)
        menu.goto(-200,30)
        menu.write("password is copied to clipboard", font=("Arial", 20))        
    else:
        pass_gen()


menu=turtle.Turtle()
menu.hideturtle()
menu.penup()
menu.goto(-300,100)
menu.write("1. generate the password", font=("Arial", 16))
menu.goto(-300,50)
menu.write("2. Exit", font=("Arial", 16))
screen.onkey(pass_gen, "1")
screen.onkey(exit,"2")

screen.listen()
turtle.mainloop()
