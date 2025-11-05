#First check lesson about while loop injection

name = input ("Press your name: ")

# 1) Create standard input: 

# if name == "" :
#     print("You did not write your name")

# else: 
#     print(f"Hello, {name}")

# 2) Create exact check:

while name == "" :
    print("You did not write your name")
    name = input ("Press your name: ")

print(f"Hello, {name}")


