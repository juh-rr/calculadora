from art import logo
# add
def add(n1, n2):
  return n1 + n2
#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  print(logo)
  keepGoing = True
  num1 = int(input("What's the first number? "))
  
  while keepGoing:
    print("Choose which operation you want to use: ")
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number? "))
    chosen_operation = operations[operation_symbol]
    answer = chosen_operation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Do you wish to continue calculating with {answer}? type 'y' or 'n': ").lower() == "y":
      num1 = answer  
    else:
      print(f"The final number is: {answer} ")
      keepGoing = False
      calculator()

calculator()
