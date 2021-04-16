class Budget:

    def __init__(self, category, balance, name):
        self.category = category
        self.balance = balance
        self.name = name

    def withdrawal(self):
        withdraw = int(input('How much do you want to withdraw: \n'))
        if withdraw > self.balance:
            print('insufficient funds')
            again = input('Do you want to try again:'
                          '\n type \'yes\' if you want to continue '
                          'else type\'no\'')
            if again == 'yes':
                welcome()
            elif again == 'no':
                exit_block()
        else:
            self.balance -= withdraw
            print(f'take your cash', withdraw, f',Your new Balance is{self.balance} ')
            exit_block()

    def fund(self):
        fund_in = int(input('enter the amount that you want to fund in: '))
        print('You entered', fund_in,)
        print(f'Your old balance is{self.balance}')
        self.balance += fund_in
        print(f'Your New Balance is {self.balance}\n')
        again = input(f'Dear {self.name} you want to perform another funding?:Y/N '.lower())
        if again == 'yes' or 'y'.lower():
            self.fund()
        elif again == 'no' or 'n'.lower():
            welcome()

    def transfer(self):
        print(f'Transfer from {self.category} budget ')
        transfer_amount = int(input('Enter amount to transfer: \n'))
        if transfer_amount >= self.balance:
            print('Insufficient funds!!!')
            exit_block()
        else:
            self.balance -= transfer_amount
            print(f'Dear {self.name} Your '
                  f'Transfer was Successful: Your new {self.category} balance is #{self.balance}')
            exit_block()

    def balance_amount(self):
        print(f"Dear {self.name}'Your'{self.category} balance is: #{self.balance}")
        exit_block()


def welcome():
    try:
        print(" WELCOME TO BUDGET APP")
        select_option = int(input('''What would you like to budget for?
    1. Food
    2. Clothing
    3. Entertainment
    4. Exit
    '''))
        if select_option == 1:
            food_sector()
        elif select_option == 2:
            clothing()
        elif select_option == 3:
            entertainment()
        elif select_option == 4:
            print("Thank you for using our budget app,\n Please call again.")
        else:
            print('Invalid Option, Try again')

    except ValueError:
        print("Try Again")
        return welcome()


def exit_block():
    try:
        bye = int(input("""Do you want to perform another transaction? \n
        1. Yes
        2. No \n
        """))
        if bye == 1:
            welcome()
        elif bye == 2:
            print('Thank You for using our app')
        else:
            print('Invalid Input, Please try again'
                  'type only numbers 1 or 2')
            welcome()
    except ValueError:
        print('Try again')
        return exit_block()


def food_sector():
    food = Budget('food', 0,name=input('what is your name?: '))
    food_Option = int(input('''Choose from the options below
        1. Fund to food budget
        2. Withdraw from food budget
        3. Transfer to another Budget
        4. Check Budget_Balance \n '''))
    if food_Option == 1:
        food.fund()
    elif food_Option == 2:
        food.withdrawal()
    elif food_Option == 3:
        transfer = int(input('''Which category would you like to transfer to?
                1.Clothing
                2.Entertainment \n'''))
        if transfer == 1:
            food.transfer()
        elif transfer == 2:
            food.transfer()
        else:
            print('invalid option')
    elif food_Option == 4:
        food.balance()
    else:
        print('invalid option selected')


def clothing():
    clothing1 = Budget('clothing',0,name=input('your  name is:'))
    print('Welcome To Clothing-Budget')
    clothing_Option = int(input('''You have the following options
        1. Fund to food budget
        2. Withdraw from food budget
        3. Transfer to another Budget
        4. Check Budget_Balance \n '''))
    if clothing_Option == 1:
        clothing1.fund()
    elif clothing_Option == 2:
        clothing1.withdrawal()
    elif clothing_Option == 3:
        category_transfer = int(input('''which category would you like to transfer to?
            1.food_sector OR
            2.Entertainment_sector \n'''))
        if category_transfer == 1:
            clothing1.transfer()
        elif category_transfer == 2:
            clothing1.transfer()
        else:
            print('invalid option')
    elif clothing_Option == 4:
        clothing1.balance()
    else:
        print('invalid option selected')
        welcome()


def entertainment():
    print('WELCOME TO ENTERTAINMENT_BUDGET_SECTOR')
    Entertainment = Budget('Entertainment',0, name=input('what is your name: '))
    Entertainment_Option = int(input('''Choose from  the following options
       1. Fund to food budget
        2. Withdraw from food budget
        3. Transfer to another Budget
        4. Check Budget_Balance \n '''))
    if Entertainment_Option == 1:
        Entertainment.fund()
    elif Entertainment_Option == 2:
        Entertainment.withdrawal()
    elif Entertainment_Option == 3:
        transfer_to = int(input('''which category would you like to transfer to?
            1.food
            2.clothing \n'''))
        if transfer_to == 1:
            Entertainment.transfer()
        elif transfer_to == 2:
            Entertainment.transfer()
        else:
            print('invalid option')
    elif Entertainment_Option == 4:
        Entertainment.balance()
    else:
        print('invalid option selected')
        welcome()


welcome()
