import random
from game.deck import Deck


class Dealer:
    """A person who directs the game. 
    
    The responsibility of a Dealer is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.card = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(1):
            deck = Deck()
            self.card.append(deck)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.deal_first_card()
        while self.is_playing:
            
            self.do_updates()
            self.get_inputs()
            self.do_outputs()

   
    def deal_first_card(self):
        """"
        Prints first value of card
        """
        self.value = random.randint(1, 13)
        print(f"The card is: {self.value} ")



    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Dealer): An instance of Dealer.
        """
        deal_card = input("Higher or Lower? [h/l] ")
        self.is_playing = (deal_card == "h" or "l")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.card)):
            card = self.card[i]
            card.deal()
            self.score += card.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.card)):
            card = self.card[i]
            values += f"{card.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)