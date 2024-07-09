from random import randint
from time import sleep
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

GAME_STATE = 0
IN_ROUND = True
WIN_RATIO = 0
ROUND_STAKE = 1
PLAYER_CARDS = []
DEALER_CARDS = []

DECK_V = {
    1: 11,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 10,
    12: 10,
    13: 10,
}

DECK_N = {
    1: "A",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
}

DECK_S = {
    1: "♠",
    2: "♣",
    3: "♥",
    4: "♦",
}


def colored_card(card_pair):
    if card_pair[1] == 1 or card_pair[1] == 2:
        return f"{Fore.WHITE}{DECK_N[card_pair[0]]}{DECK_S[card_pair[1]]}{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}{DECK_N[card_pair[0]]}{DECK_S[card_pair[1]]}{Style.RESET_ALL}"


def new_cards():
    return [[randint(1, 13), randint(1, 4)], [randint(1, 13), randint(1, 4)]]


def new_card():
    return [[randint(1, 13), randint(1, 4)]]


def print_cards(cards):
    print(f"", end="   ")
    for card in cards:
        print(f"{colored_card(card)}", end="   ")


def render_player_cards():
    print(f"   ({get_cards_value(PLAYER_CARDS)}) You")
    print(f"   ---------")
    print_cards(PLAYER_CARDS)


def render_dealer_cards():
    print(f"   ({get_cards_value(DEALER_CARDS)}) Dealer")
    print(f"   -----------")
    print_cards(DEALER_CARDS)
    if len(DEALER_CARDS) < 2:
        print("▯", end="")


def get_cards_value(cards):
    amount_of_ace = 0
    for card in cards:
        if card[0] == 1: amount_of_ace += 1

    card_totals = 0
    for card in cards:
        card_totals += DECK_V[card[0]]

    if card_totals > 21 and amount_of_ace > 0:
        while card_totals > 21 and amount_of_ace > 0:
            card_totals -= 10
            amount_of_ace -= 1

    return card_totals


# GAME LOOP
while True:
    # ROUND LOOP
    ROUND_STAKE = 1
    PLAYER_CARDS += new_cards()
    DEALER_CARDS += new_card()

    while IN_ROUND:
        os.system('cls')
        print()

        render_dealer_cards()
        print(f"\n                        WIN RATIO:    {WIN_RATIO}")
        render_player_cards()

        if get_cards_value(PLAYER_CARDS) >= 21:
            IN_ROUND = False

        else:
            print("\n\n   What do you want to do?")
            player_action = input("   (Card: c / Stand: s / Double: d): ").strip().lower()

            if player_action == "c":
                PLAYER_CARDS += new_card()

            elif player_action == "s":
                IN_ROUND = False

            elif player_action == "d":
                PLAYER_CARDS += new_card()
                ROUND_STAKE = 2
                IN_ROUND = False

    # DEALER LOOP
    while get_cards_value(DEALER_CARDS) < 17:
        DEALER_CARDS += new_card()
        os.system('cls')
        print()

        render_dealer_cards()
        print(f"\n                        WIN RATIO:    {WIN_RATIO}")
        render_player_cards()

        print("\n\n   Dealers turn...")
        sleep(0.5)
        sleep(0.5)

    # WHO WON
    os.system('cls')
    print()
    if (get_cards_value(PLAYER_CARDS) < get_cards_value(DEALER_CARDS) and get_cards_value(DEALER_CARDS) <= 21) or get_cards_value(PLAYER_CARDS) > 21:
        os.system('cls')
        print()

        render_dealer_cards()
        print(f"\n                        WIN RATIO:    {WIN_RATIO}  -{ROUND_STAKE}")
        render_player_cards()

        print("\n\n  -------------")
        print("  | YOU LOST! |")
        print("  -------------")
        WIN_RATIO -= ROUND_STAKE

    elif get_cards_value(PLAYER_CARDS) > get_cards_value(DEALER_CARDS) or get_cards_value(DEALER_CARDS) > 21:
        os.system('cls')
        print()

        render_dealer_cards()
        print(f"\n                        WIN RATIO:    {WIN_RATIO}  +{ROUND_STAKE}")
        render_player_cards()

        print("\n\n  ------------")
        print("  | YOU WON! |")
        print("  ------------")
        WIN_RATIO += ROUND_STAKE

    else:
        os.system('cls')
        print()

        render_dealer_cards()
        print(f"\n                        WIN RATIO:    {WIN_RATIO}  +-0")
        render_player_cards()

        print("\n\n  ---------")
        print("  | DRAW! |")
        print("  ---------")

    sleep(1)
    sleep(2)
    sleep(1)
    PLAYER_CARDS = []
    DEALER_CARDS = []
    IN_ROUND = True

