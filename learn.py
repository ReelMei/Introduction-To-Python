if 5 > 8:
    print("Hello World!")
else:
    print("Goodbye World!")
    
    
print("I am ",35, " Years Old")
#print("thiz is a tezt")

x = "John"
y = 10
print("my name is", x, "and i am", y, "years old")



# value = input("Enter temperature: ")
# try:
#     celsius = float(value)

#     fahrenheit = (celsius * 9 / 5) + 32

#     if celsius <= 0:
#         status = "freezing"
#     elif celsius < 20:
#         status = "cold"
#     elif celsius <= 30:
#         status = "warm"
#     else:
#         status = "hot"

#     print(f"Celsius: {celsius}")
#     print(f"Fahrenheit: {fahrenheit}")
#     print(f"Status: {status}")

# except ValueError:
#     print("Invalid temperature")



try:
    print("Hello")
except:
   print("An error occured")
   
   
   
# text = "goat"

# newtext = text.replace(" ", "").lower()

# if newtext == newtext [::-1]:
#     print("true")
# else:
#     print("false")


# left = "40"
# right = "20"
# operator = "/"

# newleft = int(left)
# newright = int(right)

# if operator == "+":
#     print(newleft + newright)
# elif operator == "-":
#     print(newleft - newright)
# elif operator == "*":
#     print(newleft * newright)
# elif operator == "/":
#     print(newleft / newright)





left = "4"
right = "2"
operator = "/"


try:
    newleft = int(left)
    newright = int(right)
except ValueError:
    print("Invalid Input")

if operator == "+":
    print(newleft + newright)
elif operator == "-":
    print(newleft - newright)
elif operator == "/":
    if newright == 0:
        print("Error: Division by zero")
elif operator == "*":
    print(newleft * newright)
else:
    print("Invalid operator")