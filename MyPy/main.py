from ops import ops
class main:
    while 1:
        a=input("L for list, A for add Q to quit\n")
        if a == 'L' or a == 'l':
            A=ops()
            i=input("Enter the ID #")
            output=A.list(id=i)
            print("Mail: \t",output['email'],"\nPassword: \t",output['password'])
        elif a == 'A' or a == 'a':
            A=ops()
            email = input("Enter the email")
            passwd = input("Enter the password")
            A.add(email,passwd)
        elif a == 'q' or a == 'Q':
            break
        else:
            print("READ")
