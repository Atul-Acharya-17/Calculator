from tkinter import *
from math import *
import tkinter.font as tkFont
from tkinter import messagebox
import matplotlib.pyplot as plt


class Calculator:
    def __init__(self, master):
        self.pi_symbol = chr(960)
        self.multiplication_symbol = chr(215)
        self.division_symbol = chr(247)
        self.exponent_symbol = 'x\u02B8'
        self.square_symbol = 'x\u00b2'
        self.two_power = '2\u02E3'
        self.euler_power = 'e\u02E3'
        self.x_inverse = 'x\u207B\u00B9'
        self.square_root = chr(8730)
        self.textEntry = ""
        self.list_expression = []
        self.algebra = True
        self.operators = (self.multiplication_symbol, self.division_symbol, "+", "-", "^", "%")
        self.features = (
            "2^", "cos(", "sin(", "tan(", "log(", "1" + self.division_symbol, "ln(", "e", "e^(", self.pi_symbol,
            self.square_root, "abs(")

        self.frame = Frame(master, width=400, height=500, background="grey", highlightbackground="red",
                           highlightthickness=1).place(relx=0.5, rely=0.5, anchor=CENTER)

        self.entryFontStyle = tkFont.Font(family="Lucida Grande", size=18)
        self.Expression = Entry(self.frame, font=self.entryFontStyle, width=25, justify="right", bg="WHITE")

        self.One = Button(self.frame, text="1", height=1, width=8, bg="BLUE",
                          command=lambda: self.appendStringExpression("1"))
        self.Two = Button(self.frame, text="2", height=1, width=8, bg="BLUE",
                          command=lambda: self.appendStringExpression("2"))
        self.Three = Button(self.frame, text="3", height=1, width=8, bg="BLUE",
                            command=lambda: self.appendStringExpression("3"))
        self.Four = Button(self.frame, text="4", height=1, width=8, bg="BLUE",
                           command=lambda: self.appendStringExpression("4"))
        self.Five = Button(self.frame, text="5", height=1, width=8, bg="BLUE",
                           command=lambda: self.appendStringExpression("5"))
        self.Six = Button(self.frame, text="6", height=1, width=8, bg="BLUE",
                          command=lambda: self.appendStringExpression("6"))
        self.Seven = Button(self.frame, text="7", height=1, width=8, bg="BLUE",
                            command=lambda: self.appendStringExpression("7"))
        self.Eight = Button(self.frame, text="8", height=1, width=8, bg="BLUE",
                            command=lambda: self.appendStringExpression("8"))
        self.Nine = Button(self.frame, text="9", height=1, width=8, bg="BLUE",
                           command=lambda: self.appendStringExpression("9"))
        self.Zero = Button(self.frame, text="0", height=1, width=18, bg="BLUE",
                           command=lambda: self.appendStringExpression("0"))
        self.Decimal = Button(self.frame, text=".", height=1, width=8, bg="BLUE",
                              command=lambda: self.appendStringExpression("."))

        self.Quit = Button(self.frame, text="Quit", bg="red", height=1, width=20, command=quit)

        self.Delete = Button(self.frame, text="DEL", height=1, width=8, bg="YELLOW",
                             command=self.popStringExpression)
        self.Clear = Button(self.frame, text="CLR", height=1, width=8, bg="YELLOW",
                            command=self.clearStringExpression)
        self.Multiply = Button(self.frame, text=self.multiplication_symbol, height=1, width=8, bg="YELLOW",
                               command=lambda: self.appendStringExpression(self.multiplication_symbol))
        self.Divide = Button(self.frame, text=self.division_symbol, height=1, width=8, bg="YELLOW",
                             command=lambda: self.appendStringExpression(self.division_symbol))
        self.Add = Button(self.frame, text="+", height=1, width=8, bg="YELLOW",
                          command=lambda: self.appendStringExpression("+"))
        self.Subtract = Button(self.frame, text="-", height=1, width=8, bg="YELLOW",
                               command=lambda: self.appendStringExpression("-"))
        self.Modulus = Button(self.frame, text="%", height=1, width=8, bg="YELLOW",
                              command=lambda: self.appendStringExpression("%"))
        self.executeAlgebra = Button(self.frame, text="EXE", height=1, width=8, bg="YELLOW",
                                     command=self.stringToList)

        self.executeGraph = Button(self.frame, text="EXE", height=1, width=8, bg="YELLOW",
                                   command=self.graphFunction)

        self.Euler = Button(self.frame, text="e", height=1, width=11, bg="GREEN",
                            command=lambda: self.appendStringExpression("e"))
        self.EulerPower = Button(self.frame, text=self.euler_power, height=1, width=11, bg="GREEN",
                                 command=lambda: self.appendStringExpression("e^("))
        self.ln = Button(self.frame, text="ln", height=1, width=11, bg="GREEN",
                         command=lambda: self.appendStringExpression("ln("))
        self.log = Button(self.frame, text="log", height=1, width=11, bg="GREEN",
                          command=lambda: self.appendStringExpression("log("))

        self.Pi = Button(self.frame, text=self.pi_symbol, height=1, width=11, bg="GREEN",
                         command=lambda: self.appendStringExpression(self.pi_symbol))
        self.sin = Button(self.frame, text="sin", height=1, width=11, bg="GREEN",
                          command=lambda: self.appendStringExpression("sin("))
        self.cos = Button(self.frame, text="cos", height=1, width=11, bg="GREEN",
                          command=lambda: self.appendStringExpression("cos("))
        self.tan = Button(self.frame, text="tan", height=1, width=11, bg="GREEN",
                          command=lambda: self.appendStringExpression("tan("))

        self.SquareRoot = Button(self.frame, text=self.square_root, height=1, width=11, bg="GREEN",
                                 command=lambda: self.appendStringExpression(self.square_root + "("))
        self.square = Button(self.frame, text=self.square_symbol, height=1, width=11, bg="GREEN",
                             command=lambda: self.appendStringExpression("^2"))
        self.XInverse = Button(self.frame, text=self.x_inverse, height=1, width=11, bg="GREEN",
                               command=lambda: self.appendStringExpression("1" + self.division_symbol))
        self.exp = Button(self.frame, text=self.exponent_symbol, height=1, width=11, bg="GREEN",
                          command=lambda: self.appendStringExpression("^("))

        self.AbsoluteValue = Button(self.frame, text="|x|", height=1, width=8, bg="GREEN",
                                    command=lambda: self.appendStringExpression("abs("))
        self.factorial = Button(self.frame, text="x!", height=1, width=8, bg="GREEN",
                                command=lambda: self.appendStringExpression("!"))
        self.TwoPower = Button(self.frame, text=self.two_power, height=1, width=8, bg="GREEN",
                               command=lambda: self.appendStringExpression("2^"))
        self.OpenBracket = Button(self.frame, text="(", height=1, width=8, bg="GREEN",
                                  command=lambda: self.appendStringExpression("("))
        self.ClosingBrcket = Button(self.frame, text=")", height=1, width=8, bg="GREEN",
                                    command=lambda: self.appendStringExpression(")"))

        self.Graph = Button(self.frame, text="Graph", height=2, width=5, bg="ORANGE", command=self.changeToGraph)

        self.Back = Button(self.frame, text="BACK", height=2, width=5, bg="ORANGE", command=self.changetoNormal)

        self.X = Button(self.frame, text="X", height=1, width=8, bg="ORANGE",
                        command=lambda: self.appendStringExpression("X"))

        self.Domain = Label(self.frame, text='Domain', height=2, width=7, bg="ORANGE")

        self.X1 = Entry(self.frame, font=self.entryFontStyle, width=3, justify="right", bg="WHITE")
        self.X2 = Entry(self.frame, font=self.entryFontStyle, width=3, justify="right", bg="WHITE")

        self.placeWidgets()

    def placeWidgets(self):
        self.Expression.place(x=205, y=140, height=65)

        self.One.place(x=180, y=400)
        self.Two.place(x=250, y=400)
        self.Three.place(x=320, y=400)
        self.Four.place(x=180, y=430)
        self.Five.place(x=250, y=430)
        self.Six.place(x=320, y=430)
        self.Seven.place(x=180, y=460)
        self.Eight.place(x=250, y=460)
        self.Nine.place(x=320, y=460)
        self.Zero.place(x=180, y=490)
        self.Decimal.place(x=320, y=490)

        self.Quit.place(x=300, y=540)

        self.Delete.place(x=415, y=400)
        self.Clear.place(x=485, y=400)
        self.Multiply.place(x=415, y=430)
        self.Divide.place(x=485, y=430)
        self.Add.place(x=415, y=460)
        self.Subtract.place(x=485, y=460)
        self.Modulus.place(x=415, y=490)
        self.executeAlgebra.place(x=485, y=490)

        self.Euler.place(x=185, y=260)
        self.EulerPower.place(x=280, y=260)
        self.ln.place(x=375, y=260)
        self.log.place(x=470, y=260)

        self.Pi.place(x=185, y=290)
        self.sin.place(x=280, y=290)
        self.cos.place(x=375, y=290)
        self.tan.place(x=470, y=290)

        self.SquareRoot.place(x=185, y=320)
        self.square.place(x=280, y=320)
        self.XInverse.place(x=375, y=320)
        self.exp.place(x=470, y=320)

        self.AbsoluteValue.place(x=185, y=350)
        self.factorial.place(x=261, y=350)
        self.TwoPower.place(x=337, y=350)
        self.OpenBracket.place(x=414, y=350)
        self.ClosingBrcket.place(x=490, y=350)

        self.Graph.place(x=490, y=210)

    def appendStringExpression(self, stringAdded):
        string = self.Expression.get()
        if stringAdded in self.features:
            try:
                if not (string[-1] in self.operators or string[-1] == "("):
                    stringAdded = self.multiplication_symbol + stringAdded
            except:
                pass
        string += stringAdded
        self.Expression.delete(0, "end")
        self.Expression.insert(0, string)

    def popStringExpression(self):
        string = self.Expression.get()
        string = string[0:-1]
        self.Expression.delete(0, "end")
        self.Expression.insert(0, string)

    def clearStringExpression(self):
        self.Expression.delete(0, "end")
        self.Expression.insert(0, "")

    def stringToList(self):
        self.list_expression = []
        string = self.Expression.get()
        position = 0
        for character in string:
            if character == "^":
                self.list_expression.append("**")
            elif character == self.multiplication_symbol:
                self.list_expression.append("*")
            elif character == self.division_symbol:
                self.list_expression.append("/")
            elif character == self.pi_symbol:
                self.list_expression.append(str(pi))
            elif character == self.square_root:
                self.list_expression.append("sqrt")
            elif character == "g":
                self.list_expression.append("g10")
            elif character == "n" and string[position - 1] == "l":
                self.list_expression.append("og")
            elif character == "!":
                self.list_expression.append("!")
                self.convertFactorial(position)
            else:
                self.list_expression.append(character)
            position = position + 1

        if self.algebra == True:
            self.calculateExpression()

    def convertFactorial(self, position):
        self.list_expression.pop(position)
        self.list_expression.insert(position, ")")
        position = position - 1
        try:
            if self.list_expression[position] == ")":
                stack = [")"]
                while len(stack) != 0:
                    position = position - 1
                    if self.list_expression[position] == ")":
                        stack.append(")")
                    elif self.list_expression[position] == "(":
                        stack.pop()
                self.list_expression.insert(position, "fact(")

            elif self.list_expression[position].isdigit():
                while self.list_expression[position - 1].isdigit():
                    position = position - 1
                self.list_expression.insert(position, "fact(")
            else:
                pass
        except:
            pass

    def calculateExpression(self):
        try:
            stringExpression = ''.join(self.list_expression)
            result = round(eval(stringExpression), 6)
            self.displayResult(str(result))
        except:
            messagebox.showerror("INVALID", "Expression is not valid\n\tOR\n Value out of Range")

    def displayResult(self, result_string):
        self.Expression.delete(0, "end")
        self.Expression.insert(0, result_string)

    def changeToGraph(self):
        self.algebra = False
        self.clearStringExpression()
        self.Graph.place_forget()
        self.Zero.place_forget()
        self.Decimal.place_forget()
        self.executeAlgebra.place_forget()
        self.Zero = Button(self.frame, text="0", height=1, width=8, bg="BLUE",
                           command=lambda: self.appendStringExpression("0"))
        self.Zero.place(x=180, y=490)
        self.Decimal.place(x=250, y=490)
        self.X.place(x=320, y=490)
        self.Back.place(x=490, y=210)
        self.Domain.place(x=205, y=210)
        self.X1.place(x=275, y=210, height=35)
        self.X2.place(x=330, y=210, height=35)
        self.executeGraph.place(x=485, y=490)

    def changetoNormal(self):
        self.algebra = True
        self.clearStringExpression()
        self.Back.place_forget()
        self.Zero.place_forget()
        self.X.place_forget()
        self.Decimal.place_forget()
        self.Domain.place_forget()
        self.X1.place_forget()
        self.X2.place_forget()
        self.executeGraph.place_forget()
        self.Zero = Button(self.frame, text="0", height=1, width=18, bg="BLUE",
                           command=lambda: self.appendStringExpression("0"))
        self.Zero.place(x=180, y=490)
        self.Decimal.place(x=320, y=490)
        self.Graph.place(x=490, y=210)
        self.executeAlgebra.place(x=485, y=490)

    def graphFunction(self):
        self.stringToList()
        try:
            x1 = float(self.X1.get())
            x2 = float(self.X2.get())
        except:
            messagebox.showerror("INVALID", "Domain not Valid")

        X = []
        y = []
        f = x1
        copy = True
        try:
            while f <= x2:
                for i, char in enumerate(self.list_expression):
                    if char == 'X':
                        if copy:
                            list = self.list_expression.copy()
                            copy = False
                        list[i] = '(' + str(f) + ')'
                try:
                    y.append(round(eval(''.join(list)), 6))
                    X.append(f)
                    copy = True
                except:
                    messagebox.showerror("INVALID", "\t   Function is not valid\n\t\tOR\n Domain specified is not the "
                                                    "domain of the function")
                    break
                f += 0.01
        except:
            pass
        if len(y) != 0:
            plt.plot(X, y, color="BLUE")
            plt.show()


window = Tk()
window.title("Calculator")
window.geometry("750x650")
calculator = Calculator(window)
window.resizable(0, 0)
window.mainloop()
