class ATM:
    def __init__(self, initial_balance = 0):
        # Initialize the ATM with an initial balance..
        self.balance = initial_balance

    def check_balance(self):
        # CHeck the current balance..
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        # Deposit money into the amount..
        if amount > 0:
            self.balance += amount
            print(f"You have successfully deposited ${amount:.2f}.")
            self.check_balance()
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        # Withdraw money from the account..
        if amount > self.balance:
            print("Insufficient funds. You connot withdraw more thean the current balance.")
        elif amount > 0:
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount:.2f}.")
            self.check_balance()
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

def main():
    # Main function to simulate the ATM operations..
    print("Welcome to the ATM!")

    # Initialise ATM with an optional starting balance
    atm = ATM(initial_balance=1000) # You can change the initial balance here.

    while True:
        print("\nPlease choose an option:")
        print("1. Check Balance")
        print("2. Deposit money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice(1/2/3/4): ")

        if choice == '1':
            atm.check_balance()

        elif choice == '2':
            try:
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == '3':
            try:
                amount = float(input("Enter the amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break                            

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()