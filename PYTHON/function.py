def greet():
    print("Welcome to pixel class!!")
greet()
#funcion with parameters
def student(name, age):
    print(f"My name is {name} and I'm {age} years old")
student("Yusra", 28)

#function using inputoutput
def add_numbers(a , b):
    return a+b
a=int(input("Enter the first number:"))
b=int("Enter the second numer:")
results = add_numbers(a, b)
print(f"the sum is {results}")

#program that gives 10% discount
def calculate_discount(price):
    discount=print*0.10
    final_price=price-discount
    return final_price
price=float(input("Enter product price"))
total=calculate_discount(price)
print(f"price after discount:{total}")
