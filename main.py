our_password = "pass123"
your_answer = ""
number_of_tries = 0
number_of_max_tries = 8

while your_answer != our_password and number_of_tries < number_of_max_tries:
    your_answer = input("Enter password: ")
    number_of_tries += 1

    if your_answer == our_password:
        print("Access granted")
        break
    else:
        remaining = number_of_max_tries - number_of_tries
        print(f"Wrong password. Attempts left: {remaining}")

if your_answer != our_password:
    print("Account blocked")
