while True:
    id=123456789
    x=123456
    iid=int(input("Enter the id here : "))
    y=int(input("Please enter your card pin : "))
    a=1000
    n=[]
    if (y==x and iid==id):
        print("Id and Pin is correct.")
        print("Enter the command such as deposit, withdraw, transaction, history and quit.")
        while True:
            z=input("Enter command here : ")
            z=z.strip()
            z=z.lower()
            if (z=="deposit"):
                print("Balance : ",a)
                b=int(input("Enter the amount : "))
                a=a+b
                print("Successfully deposited")
                print("Balance after deposited : ",a)
                g=f"Deposited : {b}"
                j=f"Balance : {a}"
                n.append(g)
                n.append(j)
            else:
                pass
            if (z=="withdraw"):
                print("Balance : ",a)
                c=int(input("Enter the amount : "))
                if (c>a):
                    print("Sorry no sufficient balance")
                else:
                    a=a-c
                    print("Successfully withdrawed")
                    print("Balance after deposited : ",a)
                    h=f"Withdraw : {c}"
                    k=f"Balance : {a}"
                    n.append(h)
                    n.append(k)
            else:
                pass
            if (z=="transaction"):
                print("Balance : ",a)
                d=int(input("Enter the amount : "))
                if (d>a):
                    print("Sorry no sufficient balance")
                else:
                    a=a-d
                    print("Successfully withdrawed")
                    print("Balance after deposited : ",a)
                    i=f"Transaction : {d}"
                    l=f"Balance : {a}"
                    n.append(i)
                    n.append(l)
            else:
                pass
            if (z=="history"):
                print("Transaction history")
                print("Initial balance : 1000")
                if (n==[]):
                    print("No transactions made yet.")
                else:
                    for m in n:
                       print(m,end="\n")
            else:
                pass
            if (z=="quit"):
                break
            else:
                pass
    else:
        print("Id or Pin is wrong.")
        print("Please try again.")

    
