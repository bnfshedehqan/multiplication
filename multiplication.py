num1=int(input("number one: "))#input for num1
num2=int(input("number two: "))#input for num2
def add_num(num1,num2):#function for multiplication
    multiply=num1*num2;
    return multiply; #return value
if (add_num(num1,num2)==64):
    print("The product is",add_num(num1,num2))#call te function
else:
    print("it's wrong .you should have entered two numbers whose product is 64. ")