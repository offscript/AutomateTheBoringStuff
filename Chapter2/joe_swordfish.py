while True:
    print("What is your name")
    name = input()
    if name != "Joe":
        continue
    print("Hello Joe. What is the password")
    password = input() 
    if password == "swordfish": #If the password does not equal swordfish the program continues, and since there is no exit condition for the while loop it just starts again 
        break
print("Welcome Joe")
        