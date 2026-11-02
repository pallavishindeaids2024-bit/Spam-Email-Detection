email = input("Enter email: ")

if "win" in email.lower() or "free" in email.lower():
    print("Spam Email")
else:
    print("Not Spam Email")