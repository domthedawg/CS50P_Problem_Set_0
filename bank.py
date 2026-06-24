#Refer to CS50P problem set 1 bank to see solution requirements
greeting = input("Greeting: ")

if greeting.startswith(("Hello", "hello")):
    print("$0")
elif greeting.startswith(("h", "H")):
    print("$20")
else:
    print("$100")