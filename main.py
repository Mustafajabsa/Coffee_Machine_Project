from MENU_RESOURCES import MENU,resources


def restart():
    global water, milk, coffee, money
    water = 300
    milk  = 200
    coffee = 100
    money = 0


restart()


def create(drink):
    
    global water, money, milk, coffee
    
    print("Please insert coins.")
    
    quaters = float(input("how many quaters?: "))*0.25
    dimes = float(input("how many dimes?: "))*0.10
    nickels = float(input("how many nickels?: "))*0.05 
    pennies = float(input("how many pennies?: "))*0.01
    money = quaters + dimes + nickels + pennies
    
    if drink == "espresso":
        if money >= MENU["espresso"]["cost"]:
            if water >= resources["water"]:
                water = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            else:
                print ("Sorry we don't have enough water!")
                play()
            if milk >= resources["milk"]:
                milk = resources["milk"]-MENU["espresso"]["ingredients"]["milk"]
            else:
                print ("Sorry we don't have enough milk")
                play()
            if coffee >= resources["coffee"]:
                coffee = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            else:
                print (f"Sorry we only have {resources['coffee']} of that type available")
                play()
            print(f"her is your ${money - MENU[drink]['cost']} in charge.")
            money = money - MENU[drink]["cost"]
            print(f"her is your {drink} ☕. Enjoy!")
            play()
       
       
        else:
            print ("Sorry that's not enough money, money refunded")
            money = 0
            play()
    
    
    elif drink == "latte":
        if money >= MENU["latte"]["cost"]:
            if water >= resources["water"]:
                water = resources["water"] - MENU["latte"]["ingredients"]["water"]
            else:
                print ("Sorry we don't have enough water!")
                play()
            if milk >= resources["milk"]:
                milk = resources["milk"]-MENU["latte"]["ingredients"]["milk"]
            else:
                print ("Sorry we don't have enough milk")
                play()
            if coffee >= resources["coffee"]:
                coffee = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            else:
                print (f"Sorry we only have {resources['coffee']} of that type available")
            print(f"her is your ${money - MENU[drink]['cost']} in charge.")
            money = money - MENU[drink]["cost"]
            print(f"her is your {drink} ☕. Enjoy!")
            play()
       
       
        else:
            print ("Sorry that's not enough money, money refunded")
            money = 0
            play()
    
    
    elif drink == "cappuccino":
        if money >= MENU["cappuccino"]["cost"]:
            if water >= resources["water"]:
                water = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            else:
                print ("Sorry we don't have enough water!")
                play()
            if milk >= resources["milk"]:
                milk = resources["milk"]-MENU["cappuccino"]["ingredients"]["milk"]
            else:
                print ("Sorry we don't have enough milk")
                play()
            if coffee >= resources["coffee"]:
                coffee = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            else:
                print (f"Sorry we only have {resources['coffee']} of that type available")
                play()
            print(f"her is your ${money - MENU[drink]['cost']} in charge.")
            money = money - MENU[drink]["cost"]
            print(f"her is your {drink} ☕. Enjoy!")
            play()
        
        
        else:
            print ("Sorry that's not enough money, money refunded")
            money = 0
            play()


def play():
    
    
    while True:
    
    
        def report():
            print(f"water : {water}ml")
            print(f"milk : {milk}ml")
            print(f"coffee : {coffee}g")
            print(f"money : {money}$")
       
       
        choice = input(" What would you like? (espresso/latte/cappuccino): ")
       
       
        if choice == "off":
            restart()
            break
        elif choice == "report":
            report()
        elif choice == "espresso":
            create(drink = "espresso")
        elif choice == "latte":
            create(drink = "latte")
        elif choice == "cappuccino":
            create(drink = "cappuccino")
play()