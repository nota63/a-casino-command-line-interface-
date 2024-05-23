# A CASINO GAME
from colorama import Fore, Style
import datetime
from plyer import notification
import random
import pandas as pd

shares = [25000, 700, 100, 678, 900]
amount_won = [3400, 677, 500, 4000, 9000, 87, 566, 766, 8000, 100000, 432, 100, 76, 899, 20]


class Game:
    def __init__(self):
        self.balance = 5000
        self.hdfc = 0
        self.stuff = []

    # function to play game

    def play(self):
        try:
            if self.balance >= 200:
                print('loading table>>>')
                data = {'Stocks': ['google', 'wipro', 'tcs', 'lenovo', 'acer'],
                        'Price': [930, 700, 100, 678, 900]
                        }
                ud = pd.DataFrame(data)
                print(data)

                user = int(input('Enter Price to purchase and Trade:'))
                shares1 = random.choice(shares)
                if user == shares:
                    amount_win = random.choice(amount_won)
                    self.balance += amount_win
                    print(Fore.LIGHTGREEN_EX + 'you Won! Congratulations!!')
                    notification.notify(
                        title='table-{}'.format(datetime.date.today()),
                        message=f"Congratulations! Your trade was correct\n you won rupees: '{amount_win}'\n keep playing!",
                        timeout=5
                    )
                else:
                    self.balance -= shares1
                    print(Fore.LIGHTRED_EX + 'You Loosed!')
                    notification.notify(
                        title='table-{}'.format(datetime.date.today()),
                        message=f"Sorry your trade was wrong!\n rupees: '{shares1}' deducted from your table account!",
                        timeout=5
                    )

            else:
                notification.notify(
                    title='table-{}'.format(datetime.date.today()),
                    message='Insufficient Funds! sorry you can not play further',
                    timeout=5
                )
        except ValueError:
            print(Fore.LIGHTRED_EX + 'valueError')
        finally:
            print('Thanks for playing table 20\n have a great day ahead!')

    # FUNCTION TO CHECK TABLE BANK MONEY
    def view_table_balance(self):
        if self.balance:
            print(Fore.LIGHTGREEN_EX + 'done! see notification instead')
            print(self.balance)
            notification.notify(
                title='table-bank-{}'.format(datetime.date.today()),
                message=f"Table Bank balance fetched successfully\n available balance: '{self.balance}'"

            )
        else:
            print('your table bank having ZERO funds please deposit some money to play')

    #         VIEW HDFC BALANCE
    def view_hdfc_balance(self):
        if self.hdfc:
            print(Fore.LIGHTGREEN_EX + 'done! check notification instead!')
            print(self.balance)
            notification.notify(
                title='hdfc-bank-{}'.format(datetime.date.today()),
                message=f"bank balance fetched successfully\n your account balance is:'{self.hdfc}'",
                timeout=5
            )
        else:
            print('Your bank having ZERO funds!')

    # DEPOSIT MONEY TO TABLE BANK
    def deposit_money_table(self):
        try:
            money = int(input('how Much To Deposit:'))
            self.balance += money
            notification.notify(
                title='-table-bank-{}'.format(datetime.date.today()),
                message=f"Rupees: {money} deposited to your table bank\n and your current balance is: '{self.balance}'"
            )
        except ValueError:
            print(Fore.LIGHTRED_EX + 'valueError')
        finally:
            print(Fore.LIGHTGREEN_EX + 'thanks for using our pay')


# SHOPPING CLASS
class Shopping(Game):
    def __init__(self):
        self.laptopscart = []
        self.phonescart = []
        super().__init__()

    # LAPTOPS CART
    def lapcart(self):
        if self.laptopscart:
            for row in self.laptopscart:
                print('your amounts you have spent on laptops>>')
                print(row)

    # PHONES CART
    def phone_cart(self):
        if self.phonescart:
            print('your money you have spent in phones>')
            for row2 in self.phonescart:
                print(row2)

# DISPLAY ITEMS/ PURCHASE LAPTOP


    def laptops(self):
     laptop_prices = {'lenovo': 25000, 'acer': 30000, 'macbook': 150000, 'ultimus': 12000, 'realme': 50000,
                     'infinix': 22000}
     while True:
        try:
            print('Press x to exit.')
            if self.balance >= 100:
                print('Available Laptops:')
                for item, price in laptop_prices.items():
                    print(f"{item}: {price}")
                user_choice = input('Enter the name of the laptop to purchase: ').lower()
                if user_choice in laptop_prices:
                    item_price = laptop_prices[user_choice]
                    if self.balance >= item_price:
                        self.laptopscart.append((user_choice, item_price))
                        self.balance -= item_price
                        print(f'{user_choice} purchased successfully!')
                        notification.notify(
                            title='-Shopping-{}'.format(datetime.date.today()),
                            message=f'Laptop purchased! {item_price} deducted from your account. Your current balance is {self.balance}',
                            timeout=5
                        )
                    else:
                        print('Insufficient balance to purchase.')
                elif user_choice == 'x':
                    print('Exiting laptops menu.')
                    break
                else:
                    print('Invalid choice! Please select from available options.')
            else:
                print('Insufficient balance to purchase.')
        except ValueError:
            print('Invalid input!')


def purchase_phones(self):
    phone_prices = {'miaow 5g': 23000, 'realm20': 50000, 'infix hot 10': 15000, 'motorola': 30000, 'vive': 23000,
                    'oppo': 12000, 'samsung': 40000}
    while True:
        try:
            print('Press x to exit.')
            if self.balance >= 100:
                print('Available Phones:')
                for item, price in phone_prices.items():
                    print(f"{item}: {price}")
                user_choice = input('Enter the name of the phone to purchase: ').lower()
                if user_choice in phone_prices:
                    item_price = phone_prices[user_choice]
                    if self.balance >= item_price:
                        self.phonescart.append((user_choice, item_price))
                        self.balance -= item_price
                        print(f'{user_choice} purchased successfully!')
                        notification.notify(
                            title='-Shopping-{}'.format(datetime.date.today()),
                            message=f'Phone purchased! {item_price} deducted from your account. Your current balance is {self.balance}',
                            timeout=5
                        )
                    else:
                        print('Insufficient balance to purchase.')
                elif user_choice == 'x':
                    print('Exiting phones menu.')
                    break
                else:
                    print('Invalid choice! Please select from available options.')
            else:
                print('Insufficient balance to purchase.')
        except ValueError:
            print('Invalid input!')


# DEFINING MAIN CLASS

def main():
    game = Game()
    shop = Shopping()

    # USER INPUT
    while True:
        try:
            user9 = int(input('press 1 to play game\n press 2 to shopping:'))
            if user9 == 1:
                menu = ("Menu\n 1]play game\n 2]deposit money to table account\n 3]view balance[table ac]\n "
                        "4]view_balance hdfc ac\n 5]quite")
                print(menu.upper())

                user10 = int(input('Enter Index to start with:'))
                if user10 == 1:
                    game.play()

                elif user10 == 2:
                    game.deposit_money_table()

                elif user10 == 3:
                    game.view_table_balance()

                elif user10 == 4:
                    game.view_hdfc_balance()

                elif user10 == 5:
                    print('leaving...done')
                    break

            elif user9 == 2:
                menu1 = ("menu>>\n 1]purchase a laptop\n 2] purchase a phone\n 3]view_laptops cart\n 4]view_phones "
                         "cart\n 5]exit")
                print(menu1.upper())

                user11 = int(input('Enter an index to shop:'))

                if user11 == 1:
                    shop.laptops()

                elif user11 == 2:
                    shop.purchase_phones()

                elif user11 == 3:
                    shop.lapcart()

                elif user11 == 4:
                    shop.phone_cart()

                elif user11 == 5:
                    print('leaving...')
                    break

        except ValueError:
            print('valueError!')
        except IndexError:
            print('index Error')
        finally:
            print('Thanks for reaching to us')


if __name__ == '__main__':
    main()
