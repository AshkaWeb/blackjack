import random

# DECK
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
deck = []


def createDeck():
    for value in values:
        for suit in suits:
            # Assigns points per card
            val = value
            col = suit
            if values.index(val) == 0:
                pts = 11
            elif values.index(val) > 9:
                pts = 10
            else:
                pts = values.index(val) + 1
            # Creates new card with correct value, color and points
            card = {'value': val, 'suit': col, 'points': pts}
            deck.append(card)

createDeck()


def blackjack(deck):

    # Number of cards
    playerCards = []
    computerCards = []

    # Scores
    playerScore = 0
    computerScore = 0


    # PLAYER'S FIRST HAND
    while len(playerCards) < 2:

        # Deals 2 cards from deck to player and sums the score
        playerCard = random.choice(deck)
        playerCards.append(playerCard['value'] + ' of ' +
                            playerCard['suit'])
        deck.remove(playerCard)
        playerScore += playerCard['points']

        # If 2 As in hand, reduces second As to 1 (Not sure it works)
        if len(playerCards) == 2:
          if playerCards[0][0] == 'A' and playerCards[1][0] == 'A':
                playerScore -= 10

    print(f"{playerName}'s hand: {playerCards} with a total of {playerScore} points")
    

    # Game over if player has 21 points
    if playerScore == 21:
        print(f"{playerName.upper()} HAS A BLACKJACK!!!!")
        print(f"DAAAAMMN {playerName.upper()} WINS!!!!")
        quit()

    # COMPUTER'S FIRST HAND
    input("Now, let's see what's my hand!")
    while len(computerCards) < 2:

        # Deals 2 cards from deck to computer and sums the score
        computerCard = random.choice(deck)
        computerCards.append(computerCard['value'] + ' of ' +
                            computerCard['suit'])
        deck.remove(computerCard)
        computerScore += computerCard['points']

        # If 2 As in hand, reduces second As to 1 (Not sure it works)
        if len(computerCards) == 2:
          if computerCards[0][0] == 'A' and computerCards[1][0] == 'A':
                computerScore -= 10

        # Prints computer's first card
        if len(computerCards) == 1:
            print(
                f"Oriane's first card: {computerCards} with {computerScore} points"
            )

    # Game over if computer has 21 points
    if computerScore == 21:
        print("ORIANE HAS A BLACKJACK!!!!")
        print(f"{playerName} LOOOOOOOOOSES!!!!")
        print(
            f"Oriane's hand: {computerCards} with a total of {computerScore} points"
        )
        quit()

    # PLAYER'S 3RD CARD
    while True:
        #if playerScore < 21:
          choice = input("Hit or Stand? (H / S): ")
          choice = choice.upper()

          # If player decides to stand, break
          if choice == 'S':
              break
          
          # If player decides to hit, deals 1 card and sums it to his total points
          if choice == 'H':
              playerCard = random.choice(deck)
              playerCards.append(playerCard['value'] + ' of ' +
                                    playerCard['suit'])
              deck.remove(playerCard)

              playerScore += playerCard['points']

              # If 2 As in hand, reduces second As to 1 (Not sure it works)
              if playerCards[0][0] == 'A' or playerCards[1][0] == 'A':
                  playerScore -= 10

              print(
                  f"{playerName}'s' hand: {playerCards} with a total of {playerScore} points"
              )
              # Game over if player has 21 points
              if playerScore == 21:
                  print(f"{playerName} HAVE A BLACKJACK!!!!")
                  print(f"DAAAAMMN {playerName} WIN!!!!")
                  quit()

              # Game over if player has more than 21 points
              if playerScore > 21:
                  print(f"{playerName} BUSTED!!!!")
                  print(f"{playerName} LOST!!!!")
                  quit()
              break

          # Ask again if invalid answer
          if (choice != 'H' and choice != 'S'):
              print("I did not understand!! Try Again")

    # COMPUTER HITS 3RD CARD IF < 17 POINTS
    input("Now, my turn")
    if computerScore < 17:
        print("Oriane decides to hit!")

        # Deals 1 card and sums it to his total points
        computerCard = random.choice(deck)
        computerCards.append(computerCard['value'] + ' of ' +
                            computerCard['suit'])
        deck.remove(computerCard)
        computerScore += computerCard['points']

        # If 2 As in hand, reduces second As to 1 (Not sure it works)
        if computerCards[0][0] == 'A' or computerCards[1][0] == 'A':
            computerScore -= 10

        # Game over if computer has 21 points
        if computerScore == 21:
            print("ORIANE HAS A BLACKJACK!!!!")
            print(f"{playerName.upper()} LOOSES!!!!")
            print(
                f"Oriane's hand: {computerCards} with a total of {computerScore} points"
            )
            quit()

        # Game over if computer has more than 21 points
        if computerScore > 21:
            print("NOOOOOO, ORIANE BUSTED!!!!")
            print(f"{playerName.upper()}'S TOO GOOD!!!!")
            quit()

    else:
        print("Oriane decides to stand!")

    # END GAME
    input("Well, let's see who won this one...")
    # Tie
    if computerScore == playerScore:
        print("IT'S A TIE!!!!")
        print(f"{playerName.upper()} GOT LUCKY, NEXT TIME WILL BE DIFFERENT!!!!")
        print(
            f"{playerName}'s hand: {playerCards} with a total of {playerScore} points"
        )
        print(
            f"Oriane's hand: {computerCards} with a total of {computerScore} points"
        )

    # Player wins
    elif playerScore > computerScore:
        print(f"{playerName.upper()} WIN!!!")
        print(f"LOOKS LIKE {playerName.upper()} WAS BETTER THAN ORIANE... BUT DON'T BE TOO COCKY!!!")
        print(
            f"{playerName}'s: {playerCards} with a total of {playerScore} points"
        )
        print(
            f"Oriane's hand: {computerCards} with a total of {computerScore} points"
        )

    # Computer wins
    else:
        print("ORIANE WIINS!!!")
        print("NO CRYING AT MY TABLE!!!")
        print(
            f"{playerName}'s hand: {playerCards} with a total of: {playerScore} points"
        )
        print(
            f"Oriane's hand: {computerCards} with a total of {computerScore} points"
        )

# PRESENTATIONS
print("Hi, I'm Oriane!")
playerName = input("What's your name?\n")
playerName = playerName.capitalize()
print(f"Hi {playerName}! Let's play blackjack!")
input("Hit enter to continue")

# GAME
while True:
    blackjack(deck)
    print("Want a rematch? ")
    rematch = input("'Y' for yes and 'N' for no: ")
    rematch = rematch.upper()
    if rematch == 'N':
        break
    if (rematch != 'Y' and rematch != 'N'):
        print("I did not understand!! Try Again")
        break
        
