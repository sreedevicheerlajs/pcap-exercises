class Deck:
    def __init__(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        # print(self.cards)

    def deal(self):
        return self.cards.pop() if len(self.cards) > 0 else None
    
    def count_remaining(self):
        return len(self.cards)
    
    def get_remaining(self):
        return [card.present() for card in self.cards]
    
    def shuffle(self):
        import random
        return random.shuffle(self.cards)


class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def present(self):
        return f"{self.value} of {self.suit}"
    
    def __str__(self):
        return f"{self.value} of {self.suit}"


# card1 = Card("hearts", "10")
# card1.present()
deck = Deck()
print(deck.get_remaining())
print(deck.count_remaining())
deck.shuffle()
print("After shuffling")
print(deck.get_remaining())
print(deck.count_remaining())
dealt_card = deck.deal()
print("Dealt card:", dealt_card)
print("Remaining cards after dealing one card:")
print(deck.count_remaining())
print(deck.get_remaining())
