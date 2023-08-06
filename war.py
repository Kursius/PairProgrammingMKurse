import random

class Card:
    def __init__(self, rank, suit, face_up=False):
        self.rank = rank
        self.suit = suit
        self.face_up = face_up

    def __repr__(self):
        if self.face_up:
            return f"{self.rank} of {self.suit}"
        else:
            return "Face Down"

    def flip(self):
        self.face_up = not self.face_up

class Deck:
    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def split_deck(self):
        half_size = len(self.cards) // 2
        return self.cards[:half_size], self.cards[half_size:]

def main():
    deck = Deck()
    player1, player2 = deck.split_deck()

if __name__ == "__main__":
    main()