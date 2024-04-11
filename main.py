import sys
import os
import time
import random
from colorama import init, Fore, Style


def get_win(win_lose, bet, coins, lines):
    if win_lose:
        winnings = bet * 2
        total_coins = coins + winnings
        print()
        print(f"{Fore.GREEN}Congratulations! You won {Fore.YELLOW}{winnings} coins.{Style.RESET_ALL}")
        print(f"Total: {Fore.YELLOW}{total_coins} coins{Style.RESET_ALL}\n")
        return total_coins
    else:
        total_coins = coins - (bet * lines)
        print(f"{Fore.RED}\nSorry, Better luck next time!\n")
        if total_coins > 0:
            print(f"you lost {bet * lines} coins.{Style.RESET_ALL}\n")
            print(f"Total: {Fore.YELLOW}{total_coins} coins{Style.RESET_ALL}\n")
        return total_coins


def check_win(matrix, lines):
    matched_lines = 0
    for row in matrix:
        if any(all(symbol == row[i] for i in range(len(row))) for symbol in row):
            matched_lines += 1
    if matched_lines >= lines:
        return True
    else:
        return False


def get_matrix(rows, cols):
    symbol_count = {" 🥝": 2, " 🍓": 4, " 🍄": 6, " 🍏": 8}

    emotrix = []
    all_symbols = []

    for symbol, count in symbol_count.items():
        for _ in range(count):
            all_symbols.append(symbol)

    for _ in range(rows):
        row = random.sample(all_symbols, cols)
        emotrix.append(row)
    return emotrix


def get_bet(bet, coins, lines):
    if bet.isdigit():
        if int(bet) > 0:
            if int(bet) * lines <= coins:
                return int(bet)
            else:
                raise ValueError(f"{Fore.RED}You don't have enough coins!{Style.RESET_ALL}\n")
        else:
            raise ValueError(f"{Fore.RED}Please enter valid number of coins!{Style.RESET_ALL}\n")
    else:
        raise ValueError(f"{Fore.RED}Please enter valid number of coins!{Style.RESET_ALL}\n")


def get_lines(initial_lines, coins):
    if initial_lines.isdigit():
        lines = int(initial_lines)
        if 0 < lines < 4:
            if 1 <= int(lines) <= 3 and (coins >= 3 or coins >= int(lines)):
                return int(lines)
            else:
                raise ValueError(f"{Fore.RED}You don't have enough coins to bet that many lines!{Style.RESET_ALL}\n")
        else:
            raise ValueError(f"{Fore.RED}Please enter valid number of lines!{Style.RESET_ALL}\n")
    else:
        raise ValueError(f"{Fore.RED}Please enter valid number of lines!{Style.RESET_ALL}\n")


def get_coins(coins):
    if coins.isdigit():
        if int(coins) > 0:
            os.system("clear" if os.name == "posix" else "cls")
            return int(coins)
        else:
            raise ValueError(f"{Fore.RED}Please enter valid number of coins!{Style.RESET_ALL}\n")
    else:
        raise ValueError(f"{Fore.RED}Please enter valid number of coins!{Style.RESET_ALL}\n")


def play_slot():
    os.system("clear" if os.name == "posix" else "cls")
    play = input(f"PRESS {Fore.YELLOW}ENTER{Style.RESET_ALL} TO PLAY!! ({Fore.YELLOW}'q'{Style.RESET_ALL} to quit) :")
    os.system("clear" if os.name == "posix" else "cls")
    if play.lower() == "q":
        sys.exit("Game closed!!\n")
    while True:
        try:
            initial_coins = input("Enter the number of coins you have: ")
            coins = get_coins(initial_coins)
            break
        except ValueError as e:
            print(f"{e}")
    print(f"Total: {Fore.YELLOW}{coins} coins{Style.RESET_ALL}")

    os.system("clear" if os.name == "posix" else "cls")
    while play.lower() != "q":
        print(f"Total: {Fore.YELLOW}{coins} coins{Style.RESET_ALL}\n")
        while True:
            try:
                initial_lines = input(f"Choose lines from {Fore.YELLOW}(1 to 3){Style.RESET_ALL} to bet: ")
                lines = get_lines(initial_lines, coins)
                break
            except ValueError as e:
                print(f"{e}")
        print()
        while True:
            try:
                initial_bet = input("How much coins to bet for each line: ")
                bet = get_bet(initial_bet, coins, lines)
                break
            except ValueError as e:
                print(f"{e}")
        os.system("clear" if os.name == "posix" else "cls")
        print(f"Total: {Fore.YELLOW}{coins} coins{Style.RESET_ALL}\n")
        print(f"Betting {Fore.YELLOW}{bet * lines} coins{Style.RESET_ALL}. Each line will cost you {Fore.YELLOW}{bet} coins{Style.RESET_ALL}.")
        print("Get ready for an exciting spin!\n")
        input(f"PRESS {Fore.YELLOW}ENTER{Style.RESET_ALL} TO SPIN!!\n")
        os.system("clear" if os.name == "posix" else "cls")
        print("The reels are spinning", end="", flush=True)
        dots = "....\n"
        for dot in dots:
            time.sleep(0.3)
            print(dot, end="", flush=True)
        print()
        rows = 3
        cols = 3
        matrix = get_matrix(rows, cols)
        print_matrix(matrix)
        win_lose = check_win(matrix, lines)
        coins = get_win(win_lose, bet, coins, lines)

        if coins <= 0:
            print(f"{Fore.RED}You have run out of coins.{Style.RESET_ALL}\n")
            break
        play = input(f"Press {Fore.YELLOW}ENTER{Style.RESET_ALL} to play again, or type {Fore.YELLOW}'q'{Style.RESET_ALL} to quit: ")
        os.system("clear" if os.name == "posix" else "cls")

    if coins != 0:
        print(f"You left with {Fore.YELLOW}{coins} coins{Style.RESET_ALL}.")
        sys.exit("Game closed!!\n")
    else:
        sys.exit("Game closed!!\n")


def print_matrix(matrix):
    for row in range(len(matrix)):
        for i, item in enumerate(matrix[row]):
            if i != len(matrix[row]) - 1:
                print(item, end="  | ")
            else:
                print(item, end="")
        print()


def main():
    init()
    play_slot()


if __name__ == "__main__":
    main()
