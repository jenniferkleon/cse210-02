import random


class Deck:
    """A collection of 52 cards

    The responsibility of the Deck is to keep track of the card calculate the points for 
    it.
   
    Attributes:
        value (int): The number on the card
    """

    def __init__(self):
        """Constructs a new instance of Deck.

        Args:
            self (): An instance of Deck.
        """
        self.value = 0
        self.points = 300

    def deal(self):
        """Generates a new random value and calculates the points for the card.
        
        Args:
            self (Die): An instance of Die.
        """
        self.value = random.randint(1,13)
        self.points = 50