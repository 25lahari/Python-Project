from tkinter import *
import tkinter as tk
from io import StringIO
import tokenize
from PIL import Image, ImageTk
import pygame
from tkvideo import tkvideo

pygame.mixer.init()
pygame.init()


def space(string):
    try:
        if " " in string:
            raise ValueError("Space is not valid")
        else:
            return True
    except ValueError as error:
        print("Error occured :", error)


def unary_minus(statement):
    try:
        if '=-' not in statement:
            return True
        else:
            raise ValueError("Unary minus is not valid")
    except ValueError as error:
        print("Error occured :", error)


def is_operator(op):
    if op == '+' or op == '-' or op == '*' or op == '%' or op == '/':
        return True
    else:
        return False


def exp_lst(exp):
    return [token[1] for token in tokenize.generate_tokens(StringIO(exp).readline) if token[1]]


def valid_expression(expression):
    c = 0
    exp = exp_lst(expression)
    for i in exp:
        if is_operator(i):
            c += 1
    try:
        if c > 1:
            raise ValueError("Invalid Expression")
        else:
            return True
    except ValueError as error:
        print("Error occured :", error)


def is_variable(var):
    try:
        if var not in ['A', 'B', 'C', 'D', 'E']:
            raise ValueError("Invalid variable name")
        else:
            return True
    except ValueError as error:
        print("Error occured :", error)


# define the interpreter function
def interpreter(statements):
    memory = {}
    for statement in statements:
        if statement == 'STOP':
            break
        if unary_minus(statement) and space(statement):
            var, expression = statement.split('=')
            if is_variable(var):
                expression = expression.strip()
                if valid_expression(expression):
                    if expression.isdigit() and int(expression) < 100:
                        memory[var] = int(expression)
                    elif '+' in expression or '-' in expression or '*' in expression or "/" in expression or "%" in expression:
                        for i in range(len(expression)):
                            if expression[i] in ['+', '-', '*','/','%']:
                                operator_index = i
                                break
                        constituent1 = expression[:operator_index].strip()
                        operator = expression[operator_index].strip()
                        constituent2 = expression[operator_index + 1:].strip()
                        # print(constituent1,operator,constituent2)
                        if operator not in ['+', '-', '*','/','%']:
                            raise ValueError("Invalid operator")
                        if constituent1.isdigit() and int(constituent1) < 100:
                            constituent1 = int(constituent1)
                        elif constituent1 in memory:
                            constituent1 = memory[constituent1]
                        else:
                            raise ValueError("Invalid constituent")
                        if constituent2.isdigit() and int(constituent2) < 100:
                            constituent2 = int(constituent2)
                        elif constituent2 in memory:
                            constituent2 = memory[constituent2]
                        else:
                            raise ValueError("Invalid constituent")
                        if operator == '+':
                            result = constituent1 + constituent2
                        elif operator == '-':
                            result = constituent1 - constituent2
                        elif operator == '*':
                            result = constituent1 * constituent2
                        elif operator == '/':
                            result = constituent1 / constituent2
                        elif operator == '%':
                            result = constituent1 % constituent2
                        memory[var] = result
                        
    sorted_dict = {key: value for key, value in sorted(memory.items())}
    result = ""
    for key, val in sorted_dict.items():
        result += key + ' = ' + str(val) + '\n'
    return result


# define GUI window for introduction
def intro_window():
    intro = tk.Tk()
    #intro.title("Interpreter Program")
    intro.geometry("1500x1500")
    intro.title("Interpreter Program")
    lblVideo = Label(intro)
    lblVideo.pack()
    player = tkvideo("C:\\Users\\LAHARI\\Downloads\\InShot_20230307_204659084.mp4", lblVideo, loop = 1, size = (1600, 800))
    player.play()

    #img = Image.open('C:\\Users\KUMAR\Pictures\\ss1.png')
    #bg = ImageTk.PhotoImage(img)
    #lbl = Label(intro, image=bg)
    #lbl.place(x=0, y=0)

    button = tk.Button(intro, text='START', font=("bold", 35), height=1, width=10, command=ifelse)
    button.place(x=100, y=350)
    button.configure(bg='coral')

    btn2 = tk.Button(intro, text='HELP', font=("bold", 35), height=1, width=10, command=menu)
    btn2.place(x=100, y=500)
    btn2.configure(bg='coral')

    def exit_intro():
        pygame.mixer.music.load("C:\\Users\\LAHARI\\Downloads\\click_s7.mp3")
        pygame.mixer.music.play(loops=0)
        intro.destroy()

    btn3 = tk.Button(intro, text='EXIT', font=("bold", 35), height=1, width=10, command=exit_intro)
    btn3.place(x=100, y=650)
    btn3.configure(bg='coral')

    intro.mainloop()


def menu():
    pygame.mixer.music.load("C:\\Users\\LAHARI\\Downloads\\click_s7.mp3")
    pygame.mixer.music.play(loops=0)
    root = Toplevel()
    root.title("MENU")
    root.geometry("1400x1450")
    img = Image.open("C:\\Users\\LAHARI\\Downloads\\Screenshot (13).png")
    bg = ImageTk.PhotoImage(img)
    lbl = Label(root, image=bg)
    lbl.place(x=0, y=0)

    def close_menu():
        pygame.mixer.music.load("C:\\Users\\LAHARI\\Downloads\\click_s7.mp3")
        pygame.mixer.music.play(loops=0)
        root.destroy()

    btn = tk.Button(root, text = "EXIT", font = ("bold", 15), height = 1, width = 8, command = close_menu)
    btn.place(x = 1400, y = 750)
    btn.configure(bg = "#C24641")
    root.mainloop()

# program for simple if-else conditions

def ifelse():
    pygame.mixer.music.load("C:\\Users\\LAHARI\\Downloads\\click_s7.mp3")
    pygame.mixer.music.play(loops=0)
    root = Toplevel()
    root.title("If-Else Condition Evaluator")
    root.geometry("1600x1600")
    img = Image.open("C:\\Users\\LAHARI\\Downloads\\WhatsApp Image 2023-03-07 at 9.55.35 PM.jpeg")
    bg = ImageTk.PhotoImage(img)
    lbl = Label(root, image=bg)
    lbl.place(x=0, y=0)

    input_label = tk.Label(root, text = "Input Conditions:", font = ("Arial", 30))
    input_label.pack(side="top", padx=10, pady=10)

    input_textbox = tk.Text(root, height = 7, font = ("Arial", 20))
    input_textbox.pack(padx = 50, pady = 10)

    evaluate_button = tk.Button(root, text="Evaluate Condition", font=("bold", 20),
                                command=lambda: evaluate_conditions())
    evaluate_button.place(x = 10, y = 330)
    evaluate_button.configure(bg = "#FBE7A1")

    evaluate_function_button = tk.Button(root, text="Evaluate Function", font=("bold", 20),
                                         command=lambda: evaluate_function())
    evaluate_function_button.place(x = 275, y = 330)
    evaluate_function_button.configure(bg = "#FBE7A1")

    interpreter_function = tk.Button(root, text="Interpret", font=("bold", 20), command=lambda: input_window())
    interpreter_function.place(x = 530, y = 330)
    interpreter_function.configure(bg = "#FBE7A1")

    output_label = tk.Label(root, text="Output:", font=("Arial", 30))
    output_label.pack(side="top", padx=10, pady=10)

    output_textbox = tk.Text(root, height=7, font=("Arial", 20))
    output_textbox.pack(padx = 50, pady = 10)

    button = Button(root, text="Close", font=("bold", 20), height = 1, width = 8, command=lambda: close_ifelse())
    button.place(x = 700, y = 700)
    button.configure(bg = "#C24641")

    def evaluate_conditions():
        pygame.mixer.music.load("C:\\Users\\LAHARI\\Downloads\\click_s7.mp3")
        pygame.mixer.music.play(loops=0)
        input_text = input_textbox.get("1.0", "end-1c")
        if "print" in input_text:
            input_text = input_text.replace("print(\"", "").replace("\")", "")
            output_text = output_textbox.insert("end", input_text + "\n")

        else:
            try:
                exec(input_text, globals())
                output_text = str(result) if 'result' in globals() else ""
            except Exception as e:
                output_text = "Error: " + str(e)
            output_textbox.delete("1.0", "end")
            output_textbox.insert("1.0", output_text)

    def evaluate_function():
        pygame.mixer.music.load("C:\\Users\\LAHARI\\Downloads\\click_s7.mp3")
        pygame.mixer.music.play(loops=0)
        input_text = input_textbox.get("1.0", "end-1c")
        try:
            exec(input_text)
        except Exception as e:
            output_text = "Error: " + str(e)
        else:
            output_text = ""
            for name, obj in locals().items():
                if callable(obj):
                    output_text += f"{name}()\n"
                    output_text += "-" * 50 + "\n"
                    try:
                        output_text += str(obj()) + "\n"
                    except Exception as e:
                        output_text += "Error: " + str(e) + "\n"
                    output_text += "-" * 50 + "\n\n"
        output_textbox.delete("1.0", "end")
        output_textbox.insert("1.0", output_text)

    # define GUI window for input and output
    def input_window():
        pygame.mixer.music.load("C:\\Users\\LAHARI\\Downloads\\click_s7.mp3")
        pygame.mixer.music.play(loops=0)
        input = Toplevel()
        img = Image.open("C:\\Users\\LAHARI\\Downloads\\WhatsApp Image 2023-03-07 at 9.55.35 PM.jpeg")
        bg = ImageTk.PhotoImage(img)
        lbl = Label(input, image=bg)
        lbl.place(x=0, y=0)
        input.title("Interpreter Program")
        input.geometry("1600x1600")
        input.configure(bg='#E6C7C2')
        input_label = tk.Label(input, text="Enter your statements below:", font=("Arial", 30))
        input_label.pack(pady=10)
        input_text = tk.Text(input, height=7, font=("Arial", 20))
        input_text.pack(padx=50, pady=10)

        execute_button = tk.Button(input, text="Execute", font=("bold", 20),
                                   command=lambda: execute(input_text.get("1.0", "end-1c")))
        execute_button.pack(pady=10)
        execute_button.configure(bg = "#FBE7A1")

        output_label = tk.Label(input, text="Output:", font=("Arial", 30))
        output_label.pack(pady=10)
        output_text = tk.Text(input, height=7, font=("Arial", 20))
        output_text.pack(padx=50, pady=10)

        button = Button(input, text="Close", font=("bold", 20), command=lambda: close_iwindow())
        button.place(x = 700, y = 720)
        button.configure(bg = "#C24641")

        def execute(statements):
            pygame.mixer.music.load("C:\\Users\\LAHARI\\Downloads\\click_s7.mp3")
            pygame.mixer.music.play(loops=0)
            output_text.delete('1.0', tk.END)
            try:
                memory = interpreter(statements.split('\n'))
                if isinstance(memory, str):
                    output_text.insert(tk.END, memory)
                else:
                    sorted_dict = {key: value for key, value in sorted(memory.items())}
                    for key, value in sorted_dict.items():
                        result = f"{key} = {value}\n"
                        output_text.insert(tk.END, result)
                output_text.insert(tk.END, "Execution successful.\n") 
                
            except Exception as e:
                output_text.insert(tk.END, f"Error: {e}\n")

        def close_iwindow():
            pygame.mixer.music.load("C:\\Users\\LAHARI\\Downloads\\click_s7.mp3")
            pygame.mixer.music.play(loops=0)
            input.destroy()

        input.mainloop()

    def close_ifelse():
        pygame.mixer.music.load("C:\\Users\\LAHARI\\Downloads\\click_s7.mp3")
        pygame.mixer.music.play(loops=0)
        root.destroy()

    root.mainloop()


# start program by opening introduction window

intro_window()
