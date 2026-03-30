Balance = 5000
users = {"insaf" : "1234", "ali" : "5678"}


def login():
    username = input("enter username: ")
    password = input("enter password: ")

    if username in users and users[username] == password:
        print("login successful")
        return True
    else:
        print("invalid username or password")
        return False

def atm():
    global Balance
    while True:
        print("\n== Welcome to the mini Atm==")
        print("1. check Balance")
        print("2. Withdraw")
        print("3. deposit")
        print("4. exit")
        try:
            choice = int(input("enter your choice: "))
            if choice == 1:
                print(f"your balance is : {Balance}")
            elif choice == 2 :
                Withdraw = int(input("enter amount to Withdraw:"))
                if Withdraw > Balance:
                    raise ValueError("insufficient Balance")
                Balance -= Withdraw
                print(f"Withdraw successful. remaining Balance: {Balance}")    
            elif choice == 3:  
                deposit = int(input("enter amount to deposit:"))      
                if deposit <= 0:
                    raise ValueError("deposit amount must be positive")
                Balance += deposit
                print(f"deposit successful. current Balance: {Balance}")
            elif choice == 4:
                print("thank you for using mini atm")    
                break
            else:
                print("invalid choice")    
        except ValueError as e:
             print(f"error: {e}")
        except Exception as e:
             print(f"error: {e}")    
        finally: print("transaction complete") 

if  login():        
    atm()
else:
    print("login failed")           