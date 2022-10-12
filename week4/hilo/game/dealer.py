from game.cards import Cards


class Dealer:
    """A Dealer who directs the game.
    The responsibility of the Dealer is to control the game.
    Attributes:
        currenCard (int): The current card value.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for the game.
    """

    def __init__(self):
        """Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.currentCard = Cards()
        self.is_playing = True
        self.score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if the next card will be higher or lower than the current card.
        Args:
            self (Dealer): an instance of Dealer.
        """
        val = self.currentCard.value
        print("The card is: %d" %val)

        # The dealer enters either h or l to continue through game loop
        dealerIn = ""
        while dealerIn != "h" or dealerIn != "l":
            dealerIn = input("Higher or lower? [h/l]: ")
            oldCard = self.currentCard
            newCard = Cards()
            if(dealerIn == "h"):
                self.get_high(oldCard, newCard)
                break

            elif(dealerIn == "l"):
                self.get_low(oldCard, newCard)
                break
            else:
                print("Invalid input")
                print()

    def do_updates(self, guess, newCard):
        """Updates the dealer's score.
        Args:
            self (Dealer): an instance of Dealer.
        """
        #updating score
        self.score += guess
        if (self.score <= 0):
            self.is_playing = False
        #updating card
        self.currentCard.value = newCard

        
    def do_outputs(self):
        """Displays the cards and the score. Also asks if the want to keep playing
        Args:
            self (Dealer): an instance of Dealer.
        """
        print(f"Next card was: {self.currentCard.value}")
        print(f"Your score is: {self.score}")
        

        if(self.score <= 0):
            self.is_playing = False
            return

        #continues loop or terminates game
        v = ""
        while v != "n" or v != "y":
            v = input("Play again [y/n]: ")
            if(v == "n"):
                self.is_playing = False
                break
            elif(v == "y"):
                print("")
                break
            else:
                print("Invalid input")


    def get_high(self, card1, card2):
        """If player chooses High and gets it right + 100 points
       If wrong - 75 points."""
        
        if card2.value > card1.value:
            self.do_updates(100, card2.value)
            
        elif card2.value < card1.value:
            self.do_updates(-75, card2.value)


    def get_low(self, card1, card2):
        """If player chooses Low and gets it right + 100 points
        If wrong - 75 points."""
        if card2.value < card1.value:
            self.do_updates(100, card2.value)
        elif card2.value > card1.value:
            self.do_updates(-75, card2.value)
        else:
            print("")
            return