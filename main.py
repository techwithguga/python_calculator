# + - * / calculator

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# multiply_function = operations["*"]
# print(multiply_function(2,3))

num1 = int(input("what's the first nymber?: "))

for symbol in operations:
    print(symbol)

should_continue = True
while should_continue:
    
    operation_symbol = input("pick an operation: ")
    num2 = int(input("what's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)

    print(f'{num1} {operation_symbol} {num2} = {answer}')

    user_input = input("Type 'y' to continue calculations, or 'n' to exit: ")
    if user_input == "y":
        num1 = answer
    else:
        should_continue = False
        
            
