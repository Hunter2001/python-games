# Blackjack game

# ========================================================================== Defining classes: card, deck, player, dealer

import random

suits = ("Clubs", "Diamonds", "Hearts", "Spades")

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck class


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    # shuffle the cards

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Participant:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_card(self, new_card):
        self.all_cards.append(new_card)

    def count_cards_value(self):
        total_value = 0
        for card in self.all_cards:
            if card.rank == 'Ace' and total_value > 10:
                total_value += 1
            else:
                total_value += card.value
        return total_value

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards.'


class Player(Participant):
    def __init__(self, name):
        Participant.__init__(self, name)

    def show_cards(self):
        print(f"{self.name}'s hand:")
        for card in self.all_cards:
            print(f'| {card} |')
        print('Total value: ', self.count_cards_value())
        print('\n')


class Dealer(Participant):
    def __init__(self, name):
        Participant.__init__(self, name)

    def show_cards(self):
        print("Dealer's hand:")
        print(f'| {self.all_cards[0]} |')
        for card in self.all_cards[1:]:
            print('| X |')
        # Show dealers cards mode
        # for card in self.all_cards[1:]:
        #     print(f'| {card.suit} {card.rank} |')
        print('Total value: ', self.count_cards_value())
        print('\n')


# ================================== HELPER FUNCTIONS

def get_chips():
    while True:
        try:
            chips = int(input('How many chips would you like to play with? '))
        except ValueError:
            print('Please enter a valid number.')
        else:
            return chips


def get_bet(chips):
    while True:
        try:
            bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Please enter a valid number.')
        else:
            if bet > chips:
                print('You do not have enough chips.')
                continue
            elif bet <= 0:
                print('Please enter a valid number.')
                continue
            else:
                return bet


def get_player_name():
    while True:
        try:
            name = input('What is your name? ')
        except ValueError:
            print('Please enter a valid name.')
        else:
            return name.capitalize()


def hit_or_stay():
    while True:
        try:
            choice = input('Would you like to hit or stay? ')
        except ValueError:
            print('Please enter a valid choice.')
        else:
            if choice.lower().startswith('h'):
                return True
            elif choice.lower().startswith('s'):
                return False
            else:
                print('Please enter a valid choice.')
                continue


def replay():
    while True:
        try:
            choice = input('Would you like to play again? ')
        except ValueError:
            print('Please enter a valid choice.')
        else:
            if choice.lower().startswith('y'):
                return True
            elif choice.startswith('n'):
                return False
            else:
                print('Please enter a valid choice.')
                continue


def show_cards(player, dealer):
    print(100 * '\n')
    player.show_cards()
    dealer.show_cards()


def get_stats():
    print('Player total value: ', player.count_cards_value())
    print('Dealer total value: ', dealer.count_cards_value())
    print('Player chips: ', chips)


# =============================== GAME LOGIC
# Setup
new_deck = Deck()
new_deck.shuffle()

print('Welcome to Blackjack!')

player = Player(get_player_name())
dealer = Dealer('Dealer')

chips = get_chips()

# ================================== GAMEPLAY
while True:

    # WHEN THE DECK IS EMPTY, SHUFFLE IT AND START A NEW GAME
    if len(new_deck.all_cards) < 12:
        new_deck = Deck()
        new_deck.shuffle()
        print('New deck shuffled!')
        print(100 * '\n')
        continue

    # RESET CARDS FOR PLAYER AND DEALER
    player.all_cards = []
    dealer.all_cards = []

    # GET BET AND SET GAME_ON TO TRUE
    bet = get_bet(chips)
    game_on = True

    # DEAL CARDS
    player.add_card(new_deck.deal_one())
    player.add_card(new_deck.deal_one())

    dealer.add_card(new_deck.deal_one())
    dealer.add_card(new_deck.deal_one())

    # Show cards
    show_cards(player, dealer)

    # Player turn
    while hit_or_stay() and game_on:
        player.add_card(new_deck.deal_one())
        show_cards(player, dealer)
        if player.count_cards_value() > 21:
            print('You busted!')
            chips -= bet
            game_on = False
            get_stats()
            break

    # Dealer turn
    while dealer.count_cards_value() < 17 and game_on:
        dealer.add_card(new_deck.deal_one())
        show_cards(player, dealer)
        if dealer.count_cards_value() > 21:
            print('Dealer busted!')
            chips += bet
            game_on = False
            get_stats()
            break

    # Who won?
    if game_on:
        if player.count_cards_value() > dealer.count_cards_value() and player.count_cards_value() <= 21:
            print('You win!')
            chips += bet
            get_stats()
        elif player.count_cards_value() == dealer.count_cards_value():
            print('It\'s a tie!')
            get_stats()
        else:
            print('Dealer wins!')
            chips -= bet
            get_stats()

    if not replay():
        break
