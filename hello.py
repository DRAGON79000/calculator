#I create a class so that the code is a lot easier to read
class operation: 
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
    def operate(self,type_of_operation):
        def add():
            added_value = self.x + self.y
            return added_value
        def subtract():
            minused_value = self.x - self.y
            return minused_value
        def multiply():
            into_value = self.x * self.y
            return into_value
        def divide():
            div_value = self.x / self.y
            return div_value
        if type_of_operation == '+':
            return add()
        elif type_of_operation == '-':
            return subtract()
        elif type_of_operation == '*':
            return multiply()
        elif type_of_operation == '/':
            return divide()
        else:
            return "sorry invalid operator."
# I create a function that basically finds the answer with the class above
def operational3(my_text):
    my_text = my_text.split()
    while len(my_text) != 1:
        equation = operation(my_text[0],my_text[2])
        answer = equation.operate(my_text[1])
        my_text.pop(0)
        my_text.pop(0)
        my_text.pop(0)
        my_text.insert(0,answer)
    answer_final = my_text[0]
    return answer
# I prompt the user for an equation
print("Hello. This is a calculator. Please type in your equation. Don't type in the equal symbol.please give a space between each number or operator.Also this calculator is useful for making small calulations only.")
my_text = input()
# I call the function that I created
print(operational3(my_text))
running = True
while running:
    my_text = input("please enter your equation.")
    print(operational3(my_text))



                
    
