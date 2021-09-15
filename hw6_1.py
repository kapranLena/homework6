
def main():
    while True:
        print("choose math action: +, - /, *, **")
        math_action = input("your action")
        if math_action in ('+', '-', '/', '*', '**'):
            x = float(input("first number"))
            y = float(input("second number"))
            if math_action == '-':
                print(x - y)
            elif math_action == '+':
                print(x + y)
            elif math_action == '*':
                print(x * y)
            elif math_action == '**':
                print(x ** y)
            elif math_action == '/':
                if y != 0:
                    print(x / y)
                else:
                    print("ATTENTION division by 0")

main()

