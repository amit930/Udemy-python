import random

suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
faces = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

play_on = True

class Card():
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
    
    def __str__(self):
        return self.face+" of "+self.suit

class Deck():
    def __init__(self):
        self.deck = [] #All possible card combinations i.e. playing list of 52 cards
        for suit in suits:
            for face in faces:
                card = Card(suit, face)
                self.deck.append(card)

    def __str__(self):
        deck_str = ''
        for c in self.deck:
            deck_str += '\n' + c.__str__()
        return deck_str

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.hasAces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.face]
        if card.face == 'Ace':
            self.hasAces += 1

    def adjustAce(self):
        while self.value > 21 and self.hasAces > 0:
            self.value -= 10
            self.hasAces -= 1

    def __str__(self):
        return "Hand value is " + str(self.value)


class Chips():
    def __init__(self, total=100):
        self.total = total
        self.bets = 0

    def win_bet(self):
        self.total += self.bets

    def lose_bet(self):
        self.total -= self.bets


def take_bet(self):
    print('\n')
    while True:
        try:
            self.bets = int(input('Enter the amount you want to bet (balance remaining: {}): '.format(self.total)))
        except:
            print('Sorry... please enter a integer!')
        else:
            if self.bets > self.total:
                print ('Insufficient funds. You have {} funds left !'.format(self.total))
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjustAce()


def hit_or_stand(deck, hand):
    global play_on
    print('\n')
    while True:
        choice = input("Do you want to hit 'h' or stand 's'?").lower();
        if choice[0] == 'h':
            hit(deck, hand)
        elif choice[0] == 's':
            print("Player stands! Dealer is playing!")
            play_on = False
        else:
            print("Wrong choice! Try again")
            continue
        break

def show_some_cards(player, dealer):
    print('\nDealers hand');
    print(' ** One card hidden **')
    print('', dealer.cards[1])
    print('\nPlayers hand', *player.cards, sep='\n ')

def show_cards(player, dealer):
    print('\nDealers hand', *dealer.cards, sep='\n ')
    print('',dealer)
    print('\nPlayers hand', *player.cards, sep='\n ')
    print('',player)

def player_busts(player,chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins(player,chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(dealer,chips):
    print("\nDealer busts!")
    chips.win_bet()
    
def dealer_wins(dealer,chips):
    print("\nDealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


######### Driver code ################

while True:
    print("\nLets play Blackjack!\n")
    print('Tips/Rules:')
    print('     1. Hit to get as close as possible to 21 without going over')
    print('     2. Dealer hits until it reaches 17')
    print('     3. First player to go over 21 loses!')
    print('\nBest of luck!!!')

    #Initialize deck
    deck = Deck()
    deck.shuffle()

    #Initialize dealer hand
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    #Initialize player hand
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    #Initialize player chips
    chips = Chips()

    take_bet(chips)

    show_some_cards(player, dealer)

    while play_on:

        hit_or_stand(deck, player)
        show_some_cards(player, dealer)

        if player.value > 21:
            player_busts(player, chips)
            break

    if player.value <= 21:

        while dealer.value < 17:
            hit(deck, dealer)

        show_cards(player, dealer)

        if dealer.value > 21:
            dealer_busts(dealer, chips) #chips are of the player

        elif dealer.value > player.value:
            dealer_wins(dealer, chips) #chips are of the player

        elif dealer.value < player.value:
            player_wins(dealer, chips) #chips are of the player

        else:
            push(player, dealer)

    #Inform abouyt player balance
    print("\nTotal player balance {}".format(chips.total))

    choice = input("\nWant to play another game 'y' for yes:").lower()
    if choice[0] == 'y':
        play_on = True
    else:
        print('\nThanks for playing')
        break;
