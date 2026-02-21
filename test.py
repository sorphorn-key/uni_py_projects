class BankAccount:
    def __init__(self, balance, name, secret):
        self.balance = balance
        self.name = name
        self.__secret = secret

    def authenticate(self, password):
        return password == self.__secret

    def gen_input(self, type=None, bank_accs=None):
        svtypes = ["electricity", "dept", "waste"]
        returns = []
        proc_acc_index = -1

        if type == 'pm':
            temp = input("Enter service type: ")
            if temp == 'b':
                return ".."
            if temp.lower() not in svtypes:
                return -1
            returns.append(temp)

        if type == 'tf':
            temp = input("Transfer to account name: ")
            if temp == 'b':
                return ".."
            i = 0
            for bank_acc in bank_accs:
                if bank_acc.name.lower() == temp.lower() and temp.lower() != self.name.lower():
                    proc_acc_index = i
                i += 1
            if proc_acc_index == -1:
                return -2
            returns.append(proc_acc_index)

        temp_amt = input("Enter the amount to proceed: ")
        if temp_amt == 'b':
            return ".."
        try:
            temp_amt = int(temp_amt)
        except ValueError:
            return -3
        if temp_amt < 100:
            return -3
        if temp_amt > self.balance and type in ["wd", "pm", "tf"]:
            return -4
        returns.append(temp_amt)

        temp_secret = input("Password: ")
        if temp_secret == 'b':
            return ".."
        if not self.authenticate(temp_secret):
            return -5

        return returns

    def deposit(self):
        while True:
            inputs = self.gen_input()

            if inputs == "..":
                print('')
                return
            if inputs == -3:
                print("Error: Invalid amount!\n")
                continue
            if inputs == -5:
                print("Error: Wrong password!\n")
                continue
            print(f"You deposited {inputs[0]} KHR to your account.\n")

            self.balance += inputs[0]
            break

    def withdraw(self):
        while True:
            inputs = self.gen_input('wd')

            if inputs == "..":
                print('')
                return
            if inputs == -3:
                print("Error: Invalid amount!\n")
                continue
            if inputs == -4:
                print("Error: Insufficient funds!\n")
                continue
            if inputs == -5:
                print("Error: Wrong password!\n")
                continue
            print(f"You withdrawn {inputs[0]} KHR from your account.\n")

            self.balance -= inputs[0]
            break

    def payment(self):
        while True:
            inputs = self.gen_input('pm')

            if inputs == "..":
                print('')
                return
            if inputs == -1:
                print("Error: Service not found!\n")
                continue
            if inputs == -3:
                print("Error: Invalid amount!\n")
                continue
            if inputs == -4:
                print("Error: Insufficient funds!\n")
                continue
            if inputs == -5:
                print("Error: Wrong password!\n")
                continue
            print(f"You paid {inputs[1]} KHR for {inputs[0]}.\n")

            self.balance -= inputs[1]
            break

    def transfer(self, bank_accs):
        while True:
            inputs = self.gen_input('tf', bank_accs)

            if inputs == "..":
                print('')
                return
            if inputs == -2:
                print("Error: Account name doesn't exist!\n")
                continue
            if inputs == -3:
                print("Error: Invalid amount!\n")
                continue
            if inputs == -4:
                print("Error: Insufficient funds!\n")
                continue
            if inputs == -5:
                print("Error: Wrong password!\n")
                continue
            print(f"You transfered {inputs[1]} KHR to {bank_accs[inputs[0]].name}.\n")

            self.balance -= inputs[1]
            bank_accs[inputs[0]].balance += inputs[1]
            break

    def status(self):
        print(f"Account name: {self.name}")
        print(f"Account Balance: {self.balance} KHR\n")

def login():
    while True:
        global logindex
        logindex = is_auth = 0
        print("Please login into an account.")
        login_name = input("Enter your account name: ")
        if login_name == 'x':
            print("Exiting...")
            exit(0)
        login_pass = input("Enter your password: ")
        if login_pass == 'x':
            print("Exiting...")
            exit(0)

        for bank in banks:
            if bank.name.lower() == login_name.lower():
                if bank.authenticate(login_pass):
                    is_auth = 1
                    break
            logindex += 1
        if is_auth == 0:
            print("Incorrect password or account name!\n")
            continue

        print(f"You logged in as {banks[logindex].name}.\n")
        print(instrct)
        while True:
            loged = command()
            if not loged:
                break

def command():
    choice = input("Await user instruction: ")
    print('')

    match choice:
        case "1":
            banks[logindex].deposit()
            return True
        case "2":
            banks[logindex].withdraw()
            return True
        case "3":
            banks[logindex].payment()
            return True
        case "4":
            banks[logindex].transfer(banks)
            return True
        case "5":
            banks[logindex].status()
            return True
        case "0":
            return False
        case "x":
            print("Exiting...")
            exit(0)
        case "h":
            print(instrct)
            return True
        case _:
            print("Error: Invalid command!\n")
            return True

logindex = 0
instrct = """1. Deposit      4. Transfer     b. Back
2. Withdraw     5. Status       x. Exit
3. Payment      0. Logout       h. Help
"""
banks = []
banks.append(BankAccount(20000, 'Dara', 'codex'))
banks.append(BankAccount(50000, 'Visal', 'catnine'))

print("=================================")
print("Welcome to Cambodia National Bank")
print("=================================\n")
while True:
    login()









