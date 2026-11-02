from datetime import datetime

def welcome():
    print('==================================================')
    print('               Welcome to GoPython!               ')
    print('==================================================')

def goodbye():
    print('==================================================')
    print('             Thank you, come again!               ')
    print('==================================================')

def invalid():
    print('==================================================')
    print('             Invalid option, try again!           ')
    print('==================================================')

def account_welcome():
    print('==================================================')
    print(f'               Welcome, {name}!           ')
    print('==================================================')

def account_balance():
    print('==================================================')
    print(f'                    ₱{balance:,.2f}              ')
    print('==================================================')

def account_savings():
    print('==================================================')
    print(f'                    ₱{savings:,.2f}              ')
    print('==================================================')

admin_name = 'Admin'
admin_pin = '1234'
balance = 100000.0
savings = 0.0
transactions = []  

while True:
    welcome()
    print('1. Log in to Account')
    print('2. Create Account')
    print('3. Exit System')

    ask = int(input('Choose an option: '))

    if ask == 1:
        name = input('Enter your username: ')
        pin = input('Enter your pin: ')

        if (name == name and pin == pin) or (name == admin_name and pin == admin_pin):
            print('Login successful!')
            print(' ')
            account_welcome()
            while True:
                print(' ')
                account_balance()
                print('1. Deposit Funds')
                print('2. Withdraw Funds')
                print('3. Savings Account')
                print('4. View Transaction History')
                print('5. Log Out')                       
                print('==================================================')
                ask = int(input('Choose an option: '))

                if ask == 1:
                    print(' ')
                    while True:
                        amount = float(input('Enter amount to deposit: '))
                        if amount <= 0:
                            print('[Error] Invalid amount entered. Please enter a valid number.')
                        elif amount > 100000.0:
                            print('[Error] Deposit amount exceeds the maximum limit.')
                        else:
                            balance += amount
                            transactions.append({
                                "type": "DEPOSIT",
                                "amount": amount,
                                "timestamp": datetime.now().strftime("%m/%d %H:%M")
                            })
                            print(f'Deposit successful! New balance: ₱{balance:,.2f}')
                            break

                elif ask == 2:
                    print(' ')
                    while True:
                        amount = float(input('Enter amount to withdraw: '))
                        if amount <= 0:
                            print('[Error] Invalid amount entered. Please enter a valid number.')
                        elif amount > 100000.0:
                            print('[Error] Withdrawal amount exceeds the maximum limit.')
                        elif amount > balance:
                            print('Insufficient funds!')
                            break
                        else:
                            balance -= amount
                            transactions.append({
                                "type": "WITHDRAWAL",
                                "amount": amount,
                                "timestamp": datetime.now().strftime("%m/%d %H:%M")
                            })
                            print(f'Withdrawal successful! New balance: ₱{balance:,.2f}')
                            break

                elif ask == 3:
                    print(' ')
                    while True:
                        print('==================================================')
                        print('                  Savings Account!                ')
                        print('==================================================')
                        account_savings()
                        print('1. Deposit Savings')
                        print('2. Withdraw Savings')
                        print('3. Log Out')
                        print('==================================================')
                        ask = int(input('Choose an option: '))

                        if ask == 1:
                            print(' ')
                            while True:
                                amount = float(input('Enter amount to deposit into savings: '))
                                if amount <= 0:
                                    print('[Error] Invalid amount entered. Please enter a valid number.')
                                elif amount > 100000.0:
                                    print('[Error] Deposit amount exceeds the maximum limit.')
                                elif amount > balance:
                                    print('Insufficient funds in main balance!')
                                    break
                                else:
                                    balance -= amount
                                    savings += amount
                                    transactions.append({
                                        "type": "SAVINGS DEP",
                                        "amount": amount,
                                        "timestamp": datetime.now().strftime("%m/%d %H:%M")
                                    })
                                    print(f'Deposit successful! New savings balance: ₱{savings:,.2f}')
                                    break

                        elif ask == 2:
                            print(' ')
                            while True:
                                amount = float(input('Enter amount to withdraw from savings: '))
                                if amount <= 0:
                                    print('[Error] Invalid amount entered. Please enter a valid number.')
                                elif amount > 100000.0:
                                    print('[Error] Withdrawal amount exceeds the maximum limit.')
                                elif amount > savings:
                                    print('Insufficient funds in savings!')
                                    break
                                else:
                                    savings -= amount
                                    balance += amount
                                    transactions.append({
                                        "type": "SAVINGS WD",
                                        "amount": amount,
                                        "timestamp": datetime.now().strftime("%m/%d %H:%M")
                                    })
                                    print(f'Withdrawal successful! New savings balance: ₱{savings:,.2f}')
                                    break

                        elif ask == 3:
                            break

                        else:
                            invalid()

                elif ask == 4:
                    print(' ')
                    print('==================================================')
                    print('               Transaction History                ')
                    print('==================================================')
                    if not transactions:
                        print("No transactions recorded yet.")
                    else:
                        print(f"{'Date/Time':<12} | {'Type':<12} | {'Amount':<10}")
                        print("-" * 38)
                        for tx in transactions[-5:]: 
                            print(f"{tx['timestamp']:<12} | {tx['type']:<12} | ₱{tx['amount']:<9,.2f}")
                    print('==================================================')

                elif ask == 5:
                    goodbye()
                    break

                else:
                    invalid()

    elif ask == 2:
        print('==================================================')
        print('               Account Creation Page              ')
        print('==================================================')
        
        name = input('Enter your username: ')
        pin = input('Enter your pin: ')
        print('Account created successfully!')
        balance = 0.0
        savings = 0.0
        transactions.clear()

    elif ask == 3:
        goodbye()
        break

    else:
        invalid()