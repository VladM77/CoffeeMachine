class coffee_machine:
    def __init__ (self, water, milk, coffee, money, cups):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        self.cups = cups

    def remaining(self):
        print("The coffee machine has:\n",
              int(self.water),"of water\n",
              int(self.milk), "of milk\n",
              int(self.coffee),
              "of coffee beans\n",
              self.cups,
              "of disposable cups\n",
              self.money, "of money")

    def fill(self):
        self.water = self.water + int(input("Write how many ml of water do you want to add:"))
        self.milk = self.milk + int(input("Write how many ml of milk do you want to add:"))
        self.coffee = self.coffee + int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups = self.cups + int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print("I gave you", self.money)
        self.money = 0

    def check_resources(self,coffee_type):
            if coffee_type == 1:
                if self.water < 250:
                    print("Not enough water!")
                elif self.coffee < 16:
                    print("Not enough coffee!")
                elif self.cups < 1:
                    print("Not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    return True
            elif coffee_type == 2:
                if self.water < 350:
                    print("Not enough water!")
                elif self.coffee < 20:
                    print("Not enough coffee!")
                elif self.milk < 75:
                    print("Not enough milk!")
                elif self.cups < 1:
                    print("Not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    return True
            elif coffee_type == 3:
                if self.water < 200:
                    print("Not enough water!")
                elif self.coffee < 12:
                    print("Not enough coffee!")
                elif self.milk < 100:
                    print("Not enough milk!")
                elif self.cups < 1:
                    print("Not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    return True
            else:
                return False

    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if choice == "1":
            if coffee_machine.check_resources(self, 1):
                self.water = self.water - 250
                self.coffee = self.coffee - 16
                self.cups -= 1
                self.money = self.money + 4
        elif choice == "2":
            if coffee_machine.check_resources(self, 2):
                self.water = self.water - 350
                self.coffee = self.coffee - 20
                self.milk = self.milk - 75
                self.cups -= 1
                self.money = self.money + 7
        elif choice == "3":
            if coffee_machine.check_resources(self,3):
                self.water = self.water - 200
                self.coffee = self.coffee - 12
                self.milk = self.milk - 100
                self.cups -= 1
                self.money = self.money + 6
        elif choice == "back":
            return

    def action(self):
        while True:
            choice = input("Write action (buy, fill, take, remaining, exit):")
            if choice == "buy":
                self.buy()
            elif choice == "fill":
                self.fill()
            elif choice == "take":
                self.take()
            elif choice == "remaining":
                self.remaining()
            elif choice == "exit":
                return


new_machine = coffee_machine(400, 540, 120, 550, 9)
new_machine.action()
