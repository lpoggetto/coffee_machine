class CoffeeMachine:
    water = 400
    coffee_beans = 120
    milk = 540
    cups = 9
    money = 550

    def ui_method(self):
        print("Write action (buy, fill, take, remaining, exit): ")
        inp = input()
        self.process_method(inp)

    def process_method(self, inp):
        if inp == "fill":
            self.fill_machine()
        elif inp == "take":
            self.take_money()
        elif inp == "remaining":
            self.start_machine()
        elif inp == "buy":
            self.make_coffee()
        elif inp == "exit":
            pass

    def start_machine(self):
        print("")
        print(f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk"
              f"\n{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups\n${self.money} of money\n")
        self.ui_method()

    def fill_machine(self):
        water_fill = int(input("Write how many ml of water do you want to add: "))
        self.water += water_fill
        milk_fill = int(input("Write how many ml of milk do you want to add: "))
        self.milk += milk_fill
        coffee_fill = int(input("Write how many grams of coffee beans do you want to add: "))
        self.coffee_beans += coffee_fill
        cups_fill = int(input("Write how many disposable cups of coffee do you want to add: "))
        self.cups += cups_fill
        self.ui_method()

    def take_money(self):
        print(f"\nI gave you ${self.money}\n")
        self.money -= self.money
        self.ui_method()

    def make_coffee(self):
        print("What do you want to buy?\n1 - espresso\n2 - latte\n3 - cappuccino")
        buy_menu = input()
        if buy_menu == "1":
            if self.water // 250 >= 1 and self.coffee_beans // 16 >= 1 and self.cups >= 1:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
            else:
                if self.water // 250 == 0:
                    print("Sorry, not enough water!\n")
                elif self.coffee_beans // 16 == 0:
                    print("Sorry, not enough coffee beans!\n")
                elif self.cups == 0:
                    print("Sorry, not enough cups!\n")
            self.ui_method()
        elif buy_menu == "2":
            if self.water // 350 >= 1 and self.milk // 75 >= 1 and self.coffee_beans // 20 >= 1 and self.cups >= 1:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
            else:
                if self.water // 350 == 0:
                    print("Sorry, not enough water!\n")
                elif self.milk // 75 == 0:
                    print("Sorry, not enough milk!\n")
                elif self.coffee_beans // 20 == 0:
                    print("Sorry, not enough coffee beans!\n")
                elif self.cups == 0:
                    print("Sorry, not enough cups!\n")
            self.ui_method()
        elif buy_menu == "3":
            if self.water // 200 >= 1 and self.milk // 100 >= 1 and self.coffee_beans // 12 >= 1 and self.cups >= 1:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
            else:
                if self.water // 200 == 0:
                    print("Sorry, not enough water!\n")
                elif self.milk // 100 == 0:
                    print("Sorry, not enough milk!\n")
                elif self.coffee_beans // 12 == 0:
                    print("Sorry, not enough coffee beans!\n")
                elif self.cups == 0:
                    print("Sorry, not enough cups!\n")
            self.ui_method()
        elif buy_menu == "back":
            self.ui_method()
        else:
            print("Wrong Input!\n")


machine = CoffeeMachine()

machine.ui_method()
