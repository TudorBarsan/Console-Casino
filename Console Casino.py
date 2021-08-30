import random
import time
import datetime


def casino_start():
    space_lines()
    print("Welcome to Tudor's Casino!")
    response = input("Are you ready to get crazy rich? (yes or no): ")
    space_lines()

    if response.lower() == "yes":
        time_delay(1)
        casino_introduction()

    elif response.lower() == "no":
        time_delay(0.5)
        print("Oh, goodbye then...")

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        casino_start()


def casino_introduction():
    global user_money

    print("That's the spirit! Before we begin, allow me to give you a rundown of how my casino works.")
    time_delay(2)
    print("To start, you will be given $1000. You can use this money to play all kinds of awesome games.")
    time_delay(2)
    print("As you play, your money will update as you win or lose.")
    time_delay(2)
    print("Before each game, you will be given instructions on how the game works so your not going in confused.")
    time_delay(2)
    print("If you are able to grow your money to $5000, you will be able to access a V.I.P. game!")
    time_delay(2)
    print("Be careful because if you lose all of your money, you won't be able to play any more games.")
    time_delay(2)
    print("Go on, I wish you the best of luck! Type the secret password 'Tudor' to continue")
    time_delay(2)
    password = input("Type the secret password here: ")
    user_money = 1000
    space_lines()

    if password.lower() == "tudor":
        casino_lobby()
        space_lines()

    else:
        time_delay(0.5)
        print("ACCESS DENIED")
        space_lines()
        casino_start()


def casino_lobby():
    print("Please type the number that corresponds with the game that you want to play \u263A")
    time_delay(1)
    space_lines()
    print("1. Random Number")
    print("2. Crash")
    print("3. Slots")
    print("4. Special Card")
    print("5. Double Your Money (V.I.P.)")
    space_lines()
    print("Type 'Exit' if you would like to leave the casino.")
    space_lines()
    time_delay(1)
    response = input("Enter here: ")
    space_lines()

    if response == "1":
        time_delay(0.5)
        random_number()

    elif response == "2":
        time_delay(0.5)
        crash()

    elif response == "3":
        time_delay(0.5)
        slots()

    elif response == "4":
        time_delay(0.5)
        special_card()

    elif response == "5":
        time_delay(0.5)
        vip_lounge()

    elif response.lower() == "exit":
        time_delay(0.5)
        casino_exit()

    else:
        time_delay(0.5)
        did_not_understand()
        space_lines()
        time_delay(1)
        casino_lobby()


def random_number():
    print("Welcome to Random Number! In this game, you will be asked to guess a random number within a certain range.")
    time_delay(2)
    print("If you guess right, you win some money, if you guess wrong, you lose your entire bet.")
    time_delay(2)
    print("You will only be allowed to guess one number and the range will be from 1, to any range you want.")
    time_delay(2)
    print("Remember, the bigger the range, the bigger the prize.")
    response = input("Are you ready to play: ")
    space_lines()
    time_delay(0.5)

    if response.lower() == "yes":
        random_number_bet()
        space_lines()
        time_delay(0.5)

    elif response.lower() == "no":
        print("Exiting Random Number...")
        casino_lobby()
        space_lines()
        time_delay(0.5)

    else:
        did_not_understand()
        space_lines()
        time_delay(0.5)
        random_number()


def random_number_bet():
    global user_bet
    global user_money

    print("How much money would you like to bet?")
    time_delay(0.5)
    space_lines()
    print("You have: ")
    show_users_money()
    time_delay(0.5)
    space_lines()
    user_bet = input("Enter integer bet here: ")
    space_lines()
    time_delay(0.5)

    if user_bet.isdigit() and 0 < int(user_bet) <= user_money:
        user_bet = int(user_bet)
        time_delay(0.5)
        random_number_range()

    else:
        print("Please enter a valid number")
        space_lines()
        time_delay(1)
        random_number_bet()


def random_number_range():
    global user_bet
    global range_high

    print(f"You've entered ${user_bet}")
    space_lines()
    time_delay(0.5)
    print("The magic number will be a random integer from 1 to an integer of your choice. (Below 1000)")
    time_delay(1)
    print("What would you like that number to be?")
    time_delay(1)
    print("Note that the bigger the number, the more money you win for guessing correctly.")
    time_delay(1)
    range_high = input("Enter the number here: ")

    if range_high.isdigit() and 1 < int(range_high) <= 1000:
        range_high = int(range_high)
        time_delay(0.5)
        space_lines()
        random_number_guess()

    else:
        time_delay(0.5)
        space_lines()
        did_not_understand()
        time_delay(0.5)
        space_lines()
        random_number_range()


def random_number_guess():
    global number_guess
    global range_high

    number_guess = input("Please enter your guess for the magic number: ")

    if number_guess.isdigit() and 1 <= int(number_guess) <= range_high:
        number_guess = int(number_guess)
        time_delay(0.5)
        space_lines()
        random_number_check_magic_number()

    else:
        time_delay(0.5)
        space_lines()
        did_not_understand()
        time_delay(0.5)
        space_lines()
        random_number_guess()


def random_number_check_magic_number():
    global number_guess
    global range_high
    global user_money

    magic_number = random.randint(1, range_high)
    time_delay(0.5)
    space_lines()
    print("The magic number is... ", end="")
    time_delay(1)
    print(f"{magic_number}")

    if magic_number == number_guess:
        time_delay(0.5)
        space_lines()
        random_number_win()

    elif magic_number != number_guess and (user_money - user_bet) > 0:
        time_delay(0.5)
        space_lines()
        random_number_loss()

    else:
        time_delay(0.5)
        space_lines()
        user_broke()


def random_number_win():
    global range_high
    global user_bet
    global user_money

    money_won = user_bet * range_high
    user_money += money_won

    print(f"Congratulations, you won ${money_won}  \u263A")
    time_delay(1)
    print("You now have: ")
    time_delay(0.5)
    show_users_money()
    time_delay(1.5)
    space_lines()
    response = input("Would you like to play Random Number again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        random_number_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        user_money -= money_won
        time_delay(1)
        space_lines()
        random_number_win()


def random_number_loss():
    global range_high
    global user_bet
    global user_money

    print(f"Sorry, you lost ${user_bet} \u2639")
    time_delay(1)
    user_money -= user_bet
    print("You now have: ")
    time_delay(0.5)
    show_users_money()
    time_delay(1.5)
    space_lines()
    response = input("Would you like to play Random Number again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        random_number_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        user_money += user_bet
        time_delay(1)
        space_lines()
        random_number_loss()


def crash():
    print("Welcome to Crash, in this game you will place a bet to enter the round.")
    time_delay(2)
    print("Once the round starts, your money will increase as time goes on.")
    time_delay(2)
    print("You can pull out your bet at any point in the round to lock in your profits at the current time.")
    time_delay(2)
    print("However, if you pull out your money too late, you will lose it all.")
    time_delay(2)
    response = input("Are you ready to play: ")
    space_lines()
    time_delay(0.5)

    if response.lower() == "yes":
        crash_bet()
        space_lines()
        time_delay(0.5)

    elif response.lower() == "no":
        print("Exiting Crash ...")
        casino_lobby()
        space_lines()
        time_delay(0.5)

    else:
        did_not_understand()
        space_lines()
        time_delay(0.5)
        crash()


def crash_bet():
    global user_bet
    global user_money

    print("How much money would you like to bet?")
    time_delay(0.5)
    space_lines()
    print("You have: ")
    show_users_money()
    time_delay(0.5)
    space_lines()
    user_bet = input("Enter integer bet here: ")
    space_lines()
    time_delay(0.5)

    if user_bet.isdigit() and 0 < int(user_bet) <= user_money:
        user_bet = int(user_bet)
        time_delay(0.5)
        space_lines()
        crash_round_start()

    else:
        print("Please enter a valid number")
        space_lines()
        time_delay(1)
        crash_bet()


def crash_round_start():
    global user_bet

    print(f"You've entered ${user_bet}")
    time_delay(0.5)
    print("Once the round starts, you can pull out your bet at any time by pressing the enter key.")
    time_delay(1)
    space_lines()
    response = input("Type 'start' to begin the next round: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "start":
        crash_round()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        crash_round_start()


def crash_round():
    global start_time
    global user_time
    global crash_time
    global user_money
    global user_bet

    crash_time = random.randint(1, 13)
    start_time = datetime.datetime.now()
    response = input("Round is in progress: ")
    user_time = get_elapsed_time_seconds()
    user_time += 1
    time_delay(1)
    space_lines()

    if user_time < crash_time:
        crash_win()

    elif user_time >= crash_time and (user_money - user_bet) > 0:
        crash_loss()

    else:
        user_broke()


def crash_win():
    global user_time
    global crash_time
    global user_bet
    global user_money

    print("Congratulations!")
    time_delay(0.5)
    print(f"You pulled out at {user_time} seconds, the round was going to crash at {crash_time} seconds.")
    time_delay(2)
    money_won = user_bet * (user_time - 1)
    print(f"You just won ${money_won} !")
    user_money += money_won
    time_delay(1)
    space_lines()
    print("You now have:")
    show_users_money()
    time_delay(1.5)
    space_lines()
    response = input("Would you like to play Crash again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        crash_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        user_money -= money_won
        crash_win()


def crash_loss():
    global user_time
    global crash_time
    global user_bet
    global user_money

    print(f"CRASH! Oh, no you pulled out too late \u263A")
    time_delay(0.5)
    print(f"You pulled out at {user_time} seconds, the round crashed at {crash_time} seconds.")
    time_delay(2)
    print(f"You lost ${user_bet}")
    user_money -= user_bet
    time_delay(1)
    space_lines()
    print("You now have:")
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Crash again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        crash_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        time_delay(1)
        user_money += user_bet
        space_lines()
        crash_loss()


def slots():
    print("Welcome to Slots.")
    time_delay(0.5)
    print("In this game you must make a bet in order to get a spin at the slot machine.")
    time_delay(2)
    print("The slot machine will output 3 numbers from 1-9.")
    time_delay(1.5)
    print("If none of the numbers match, you lose your entire bet.")
    time_delay(1.5)
    print("If two of the numbers match, you win back 2 times your bet.")
    time_delay(1.5)
    print("If all three of the numbers match, you win back 5 times your bet!")
    time_delay(1.5)
    print("There are also * characters that are special.")
    time_delay(1.5)
    print("If you get one * character, you win back 2 times your bet.")
    time_delay(1.5)
    print("If you get two * characters you win back 5 times your bet.")
    time_delay(1.5)
    print("If you get all three * characters, you win back 10 times your bet!")
    time_delay(1.5)
    response = input("Are you ready to play: ")
    space_lines()
    time_delay(0.5)

    if response.lower() == "yes":
        slots_bet()
        space_lines()
        time_delay(0.5)

    elif response.lower() == "no":
        print("Exiting Slots ...")
        space_lines()
        casino_lobby()
        space_lines()
        time_delay(0.5)

    else:
        did_not_understand()
        space_lines()
        time_delay(0.5)
        slots()


def slots_bet():
    global user_bet
    global user_money

    print("How much money would you like to bet?")
    time_delay(0.5)
    space_lines()
    print("You have: ")
    show_users_money()
    time_delay(0.5)
    space_lines()
    user_bet = input("Enter integer bet here: ")
    space_lines()
    time_delay(0.5)

    if user_bet.isdigit() and 0 < int(user_bet) <= user_money:
        user_bet = int(user_bet)
        slots_round_start()

    else:
        print("Please enter a valid number")
        space_lines()
        time_delay(1)
        slots_bet()


def slots_round_start():
    global user_bet

    print(f"You've entered ${user_bet}")
    space_lines()
    time_delay(1)
    print("Spin the slot machine by typing 'Spin' and then pressing the enter key")
    space_lines()
    time_delay(1)
    response = input("Type 'Spin' to spin the slot machine: ")

    if response.lower() == "spin":
        slots_round()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        slots_round_start()


def slots_round():
    slot_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*"]
    print("The slot machine is spinning...")
    space_lines()
    time_delay(3)
    number_1 = random.choice(slot_options)
    number_2 = random.choice(slot_options)
    number_3 = random.choice(slot_options)
    print(f"  {number_1}  ", end="")
    time_delay(2)
    print(f"{number_2}  ", end="")
    time_delay(2)
    print(f"{number_3}  ")
    space_lines()
    time_delay(2)

    if number_1 == number_2 == number_3 and number_1 != "*":
        slots_won_5x_pair()

    elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
        slots_won_2x_pair()

    elif number_1 == "*" and number_2 == "*" and number_3 == "*":
        slots_won_10x_star()

    elif number_1 == "*" and number_1 == number_2 or number_1 == "*" and number_1 == number_3 or number_2 == "*" and number_2 == number_3:
        slots_won_5x_star()

    elif number_1 == "*" or number_2 == "*" or number_3 == "*":
        slots_won_2x_star()

    elif number_1 != number_2 != number_3 and number_1 != number_2 != number_3 != "*" and (user_money - user_bet) > 0:
        slots_loss()

    else:
        user_broke()


def slots_won_2x_pair():
    global user_bet
    global user_money

    print("Congratulations, you matched a pair!")
    time_delay(1)
    print("You won 2x your money")
    money_won = 2 * user_bet
    user_money += money_won
    time_delay(1)
    print(f"You just won ${money_won} !")
    time_delay(1)
    space_lines()
    print("You now have: ")
    space_lines()
    time_delay(0.5)
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Slots again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        slots_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        user_money -= money_won
        slots_won_2x_pair()


def slots_won_2x_star():
    global user_bet
    global user_money

    print("Congratulations, you got a star!")
    time_delay(1)
    print("You won 2x your money")
    money_won = 2 * user_bet
    user_money += money_won
    time_delay(1)
    print(f"You just won ${money_won} !")
    time_delay(1)
    space_lines()
    print("You now have: ")
    space_lines()
    time_delay(0.5)
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Slots again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        slots_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        user_money -= money_won
        slots_won_2x_star()


def slots_won_5x_pair():
    global user_bet
    global user_money

    print("Congratulations, you matched a all three numbers!")
    time_delay(1)
    print("You won 5x your money")
    money_won = 5 * user_bet
    user_money += money_won
    time_delay(1)
    print(f"You just won ${money_won} !")
    time_delay(1)
    space_lines()
    print("You now have: ")
    space_lines()
    time_delay(0.5)
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Slots again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        slots_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        user_money -= money_won
        slots_won_5x_pair()


def slots_won_5x_star():
    global user_bet
    global user_money

    print("Congratulations, you matched 2 stars!")
    time_delay(1)
    print("You won 5x your money")
    money_won = 5 * user_bet
    user_money += money_won
    time_delay(1)
    print(f"You just won ${money_won} !")
    time_delay(1)
    space_lines()
    print("You now have: ")
    space_lines()
    time_delay(0.5)
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Slots again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        slots_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        user_money -= money_won
        slots_won_5x_star()


def slots_won_10x_star():
    global user_bet
    global user_money

    print("Congratulations, you matched all three stars!")
    time_delay(1)
    print("You won 10x your money")
    money_won = 10 * user_bet
    user_money += money_won
    time_delay(1)
    print(f"You just won ${money_won} !")
    time_delay(1)
    space_lines()
    print("You now have: ")
    space_lines()
    time_delay(0.5)
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Slots again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        slots_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        user_money -= money_won
        slots_won_10x_star()


def slots_loss():
    global user_bet
    global user_money

    print(f"Unlucky, you did not match anything \u2639")
    time_delay(1)
    print(f"You just lost ${user_bet}")
    user_money -= user_bet
    time_delay(1)
    space_lines()
    print("You now have: ")
    space_lines()
    time_delay(0.5)
    show_users_money()
    space_lines()
    response = input("Would you like to play Slots again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        slots_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        user_money += user_bet
        time_delay(1)
        space_lines()
        slots_loss()


def special_card():
    print("Welcome to Special Card. In this game you will pick a card from a deck of 54 cards.")
    time_delay(1)
    print("Then a special card will also be picked from a full deck of 54 cards.")
    time_delay(1)
    print("You will win money based on how your card relates to the special card.")
    time_delay(1)
    print("The rewards are as follows:")
    time_delay(0.5)
    space_lines()
    print("Same suit - Win 2x  bet")
    print("Same number - Win 3x bet")
    print("Same card - Win 5x bet")
    print("Joker - Win 10x bet")
    print("No relation - Lose bet")
    time_delay(2)
    space_lines()
    response = input("Are you ready to play: ")
    space_lines()
    time_delay(0.5)

    if response.lower() == "yes":
        special_card_bet()

    elif response.lower() == "no":
        print("Exiting Special Card ...")
        casino_lobby()

    else:
        did_not_understand()
        space_lines()
        time_delay(0.5)
        special_card()


def special_card_bet():
    global user_bet
    global user_money

    print("How much money would you like to bet?")
    time_delay(0.5)
    space_lines()
    print("You have: ")
    show_users_money()
    time_delay(0.5)
    space_lines()
    user_bet = input("Enter integer bet here: ")
    space_lines()
    time_delay(0.5)

    if user_bet.isdigit() and 0 < int(user_bet) <= user_money:
        user_bet = int(user_bet)
        special_card_value_pick()

    else:
        print("Please enter a valid number")
        space_lines()
        time_delay(1)
        special_card_bet()


def special_card_value_pick():
    global user_bet
    global card_value
    global suit_value

    value_options = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "k", "q", "a"]

    print(f"You've entered ${user_bet}")
    space_lines()
    time_delay(1)
    print("Please enter the card value you would like to pick (no suit yet).")
    space_lines()
    time_delay(1)
    print("For a number card, just enter the number. For a...")
    space_lines()
    time_delay(0.5)
    print("Jack, enter 'J'")
    print("Queen, enter 'Q'")
    print("King, enter 'K'")
    print("Ace, enter 'A'")
    print("Joker, enter 'JO'")
    space_lines()
    time_delay(1)
    card_value = input("Enter the card value here: ")

    if card_value.lower() in value_options:
        space_lines()
        time_delay(1)
        special_card_suit_pick()

    elif card_value.lower() == "jo":
        suit_value = ""
        space_lines()
        time_delay(1)
        special_card_start()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        special_card_value_pick()


def special_card_suit_pick():
    global suit_value

    suit_options = ["h", "d", "c", "s"]
    print("Please enter the suit you would like you pick.")
    time_delay(0.5)
    space_lines()
    print("Hearts enter 'H'")
    print("Diamonds enter 'D'")
    print("Clubs enter 'C'")
    print("Spades enter 'S'")
    time_delay(1)
    space_lines()
    suit_value = input("Enter the suit here: ")

    if suit_value.lower() in suit_options:
        space_lines()
        time_delay(1)
        special_card_start()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        special_card_suit_pick()


def special_card_start():
    global card_value
    global suit_value
    global user_card

    print(f"Your card is {card_value.upper()} of {suit_value.upper()}")
    user_card = f"{card_value.lower()}{suit_value.lower()}"
    space_lines()
    time_delay(1)
    response = input("To pick the special card type 'Pick' and then press the enter key: ")

    if response.lower() == "pick":
        space_lines()
        time_delay(0.5)
        special_card_chosen()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        special_card_start()


def special_card_chosen():
    global user_card
    global user_money
    global user_bet

    card_options = ["2d", "2h", "2c", "2s", "3d", "3h", "3c", "3s", "4d", "4h", "4c", "4s", "5d", "5h", "5c", "5s", "6d", "6h", "6c", "6s", "7d", "7h", "7c", "7s", "8d", "8h", "8c", "8s", "9d", "9h", "9c", "9s", "10d", "10h", "10c", "10s", "jd", "jh", "jc", "js", "qd", "qh", "qc", "qs", "kd", "kh", "kc", "ks", "ad", "ah", "ac", "as", "jo", "jo"]
    special_card_picked = random.choice(card_options)

    print(f"The special card is", end="")
    time_delay(0.6)
    print(".", end="")
    time_delay(0.6)
    print(".", end="")
    time_delay(0.6)
    print(".  ", end="")
    time_delay(0.6)
    print(f"{special_card_picked.upper()}")
    time_delay(1)
    space_lines()

    if user_card == "jo" and special_card == "jo":
        special_card_won_10x()

    elif (user_card[0] == special_card_picked[0] or user_card[:-1] == special_card_picked[:-1]) and user_card[-1] == special_card_picked[-1]:
        special_card_won_5x()

    elif user_card[0] == special_card_picked[0] or user_card[:-1] == special_card_picked[:-1]:
        special_card_won_3x()

    elif user_card[-1] == special_card_picked[-1]:
        special_card_won_2x()

    elif user_card[0] != special_card_picked[0] and user_card[:-1] != special_card_picked[:-1] and user_card[-1] != special_card_picked[-1] and user_card != "jo" and special_card_picked != "jo" and user_money - user_bet > 0:
        special_card_lose()

    else:
        user_broke()


def special_card_won_10x():
    global user_bet
    global user_money

    print("Congratulations, your card relates to the special card since they are both jokers!")
    time_delay(1)
    print("You won 10x your bet")
    time_delay(0.5)
    money_won = user_bet * 10
    print(f"You just won ${money_won} !")
    user_money += money_won
    time_delay(0.5)
    space_lines()
    print("You now have: ")
    space_lines()
    time_delay(0.5)
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Special Card again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        special_card_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        user_money -= money_won
        special_card_won_10x()


def special_card_won_5x():
    global user_bet
    global user_money

    print("Congratulations, your card relates to the special card since they are the same card!")
    time_delay(1)
    print("You won 5x your bet")
    time_delay(0.5)
    money_won = user_bet * 5
    print(f"You just won ${money_won} !")
    user_money += money_won
    time_delay(0.5)
    space_lines()
    print("You now have: ")
    space_lines()
    time_delay(0.5)
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Special Card again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        special_card_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        user_money -= money_won
        special_card_won_5x()


def special_card_won_3x():
    global user_bet
    global user_money

    print("Congratulations, your card relates to the special card since they are the same value")
    time_delay(1)
    print("You won 3x your bet")
    time_delay(0.5)
    money_won = user_bet * 3
    print(f"You just won ${money_won} !")
    user_money += money_won
    time_delay(0.5)
    space_lines()
    print("You now have: ")
    space_lines()
    time_delay(0.5)
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Special Card again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        special_card_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        user_money -= money_won
        special_card_won_3x()


def special_card_won_2x():
    global user_bet
    global user_money

    print("Congratulations, your card relates to the special card since they are the same suit!")
    time_delay(1)
    print("You won 2x your bet")
    time_delay(0.5)
    money_won = user_bet * 2
    print(f"You just won ${money_won} !")
    user_money += money_won
    time_delay(0.5)
    space_lines()
    print("You now have: ")
    space_lines()
    time_delay(0.5)
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Special Card again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        special_card_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        user_money -= money_won
        special_card_won_2x()


def special_card_lose():
    global user_bet
    global user_money

    print("Unlucky, your card does not relate to the special card \u2639")
    time_delay(1)
    print("You lost your bet")
    user_money -= user_bet
    time_delay(0.5)
    space_lines()
    print("You now have: ")
    space_lines()
    time_delay(0.5)
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Special Card again: ")
    time_delay(0.5)
    space_lines()

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        special_card_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        user_money += user_bet
        time_delay(1)
        space_lines()
        special_card_lose()


def vip_lounge():
    global user_money

    print("Travelling to the V.I.P lounge...")
    time_delay(1)
    space_lines()

    if user_money >= 5000:
        double_your_money()

    else:
        print("Looks like you don't have enough money to enter the V.I.P lounge.")
        time_delay(1)
        print("Grow your money to $5000 in order to become a V.I.P. member.")
        time_delay(1)
        space_lines()
        time_delay(1)
        print("Exiting the V.I.P. lounge...")
        time_delay(1)
        space_lines()
        casino_lobby()


def double_your_money():
    print("Welcome to the V.I.P. lounge! Here you can play a V.I.P. exclusive game called Double Your Money.")
    time_delay(1)
    print("This game is very simple and straightforward.")
    time_delay(1)
    print("You will make a bet and then choose 3 numbers on a 6 sided die.")
    time_delay(1)
    print("The die will then be rolled once, and if one of your numbers is rolled, you double your money!")
    time_delay(1)
    print("If none of your numbers are rolled, you lose your entire bet.")
    time_delay(1)
    response = input("Are you ready to play: ")
    time_delay(1)
    space_lines()

    if response.lower() == "yes":
        double_your_money_bet()

    elif response.lower() == "no":
        print("Exiting Double Your Money ...")
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        space_lines()
        time_delay(0.5)
        double_your_money()


def double_your_money_bet():
    global user_bet
    global user_money

    print("How much money would you like to bet?")
    time_delay(0.5)
    space_lines()
    print("You have: ")
    show_users_money()
    time_delay(0.5)
    space_lines()
    user_bet = input("Enter integer bet here: ")
    space_lines()
    time_delay(0.5)

    if user_bet.isdigit() and 0 < int(user_bet) <= user_money:
        user_bet = int(user_bet)
        double_your_money_pick_1()

    else:
        print("Please enter a valid number")
        space_lines()
        time_delay(1)
        double_your_money_bet()


def double_your_money_pick_1():
    global user_bet
    global num_1
    global number_options

    number_options = ["1", "2", "3", "4", "5", "6"]
    print(f"You've entered ${user_bet}")
    time_delay(1)
    space_lines()
    print("Please pick the first number on the die (1 - 6)")
    num_1 = input("Enter number here: ")
    time_delay(1)
    space_lines()

    if num_1 in number_options:
        number_options.remove(num_1)
        double_your_money_pick_2()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        double_your_money_pick_1()


def double_your_money_pick_2():
    global number_options
    global num_1
    global num_2

    print("Please pick the second number on the die (1 - 6)")
    time_delay(1)
    num_2 = input("Enter number here: ")
    time_delay(1)
    space_lines()

    if num_2 in number_options:
        number_options.remove(num_2)
        double_your_money_pick_3()

    elif num_2 == num_1:
        print("You already picked that number")
        time_delay(1)
        space_lines()
        double_your_money_pick_2()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        double_your_money_pick_2()


def double_your_money_pick_3():
    global number_options
    global num_1
    global num_2
    global num_3

    print("Please pick the third number on the die (1 - 6)")
    time_delay(1)
    num_3 = input("Enter number here: ")
    time_delay(1)
    space_lines()

    if num_3 in number_options:
        double_your_money_start()

    elif num_3 == num_1 or num_3 == num_2:
        print("You already picked that number")
        time_delay(1)
        space_lines()
        double_your_money_pick_3()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        double_your_money_pick_3()


def double_your_money_start():
    global num_1
    global num_2
    global num_3

    print(f"You picked numbers: {num_1}, {num_2} and {num_3}")
    time_delay(1)
    space_lines()
    response = input("Roll the magic die by typing 'Roll' and then pressing the enter key: ")
    time_delay(1)
    space_lines()

    if response.lower() == "roll":
        space_lines()
        time_delay(0.5)
        double_your_money_roll()

    else:
        did_not_understand()
        time_delay(1)
        space_lines()
        double_your_money_start()


def double_your_money_roll():
    global num_1
    global num_2
    global num_3
    global special_number
    global user_money
    global user_bet

    special_number = random.randint(1, 6)
    print("The magic number rolled is", end="")
    time_delay(1)
    print(".", end="")
    time_delay(1)
    print(".", end="")
    time_delay(1)
    print(". ", end="")
    time_delay(1)
    print(f"{special_number} !")
    time_delay(1)
    space_lines()

    if special_number == int(num_1) or special_number == int(num_2) or special_number == int(num_3):
        double_your_money_win()

    elif special_number != int(num_1) and special_number != int(num_2) and special_number != int(num_3) and (user_money - user_bet) > 0:
        double_your_money_loss()

    else:
        user_broke()


def double_your_money_win():
    global special_number
    global user_bet
    global user_money

    print(f"Congratulations! You matched the number {special_number} \u263A")
    time_delay(1)
    space_lines()
    money_won = user_bet * 2
    user_money += user_bet
    print(f"You just doubled your money and won ${money_won}")
    time_delay(1)
    space_lines()
    print("You now have:")
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Double Your Money again: ")

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        double_your_money_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        user_money -= money_won
        time_delay(1)
        space_lines()
        double_your_money_win()


def double_your_money_loss():
    global special_number
    global user_bet
    global user_money

    print(f"Unlucky, none of your numbers matched with {special_number} \u2639")
    time_delay(1)
    space_lines()
    user_money -= user_bet
    print(f"You lost  ${user_bet}")
    time_delay(1)
    space_lines()
    print("You now have:")
    show_users_money()
    time_delay(1)
    space_lines()
    response = input("Would you like to play Double Your Money again: ")

    if response.lower() == "yes":
        print("Awesome!")
        time_delay(0.5)
        space_lines()
        double_your_money_bet()

    elif response.lower() == "no":
        print("Returning to casino lobby...")
        time_delay(2)
        space_lines()
        casino_lobby()

    else:
        did_not_understand()
        user_money += user_bet
        time_delay(1)
        space_lines()
        double_your_money_loss()


def casino_exit():
    print(f"You finished with ${user_money}!")
    print("We hope you enjoyed Tudor's Casino!")


def show_users_money():
    print("*" * (len(str(user_money)) + 5))
    print(f"* ${user_money} *")
    print("*" * (len(str(user_money)) + 5))


def get_elapsed_time_seconds():
    global start_time

    current_time = datetime.datetime.now()
    elapsed_time = datetime.datetime(1, 1, 1) + abs(start_time - current_time)
    return elapsed_time.second


def user_broke():
    global user_money
    global user_bet

    print(f"Oh no, you lost {user_bet} \u2639")
    user_money -= user_bet
    time_delay(1)
    space_lines()
    print("You now have:")
    show_users_money()
    time_delay(1)
    space_lines()
    print("You don't have any more money. You must now exit the Casino")
    time_delay(2)
    space_lines()
    casino_exit()


def did_not_understand():
    print("Sorry, I didn't understand.")


def space_lines():
    print("")


def time_delay(seconds):
    time.sleep(seconds)


# MAIN
casino_start()
