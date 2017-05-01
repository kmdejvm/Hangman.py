import random 
# 1. Ask player if they want to play hangman?
# - ask for user input "Do you want to play Hangman with me?" 
# - player can select y or n
# - if y, play hangman
# - if n, print "maybe we can play later" then return question

def asking_to_play_game():
    """asks player if they want to play"""
    prompt = "\nDo you want to play Hangman with me, yes or no? \n>>>"
    yes_or_no = raw_input(prompt)
    if yes_or_no == "yes":
        print "Guess a letter!"
        correct_word = pick_a_word()
        print "Your word is", str(len(correct_word)), "characters long"
    else:
        print "Maybe we can play later!"

# 2. Choose secret word 
def pick_a_word():
    """asks player if they want to pick a word""" 
    my_list = ['learning', 'growing', 'changing', 'living']
    word = random.choice(my_list)
    print word #keeping this in for trouble-shooting will remove for actual game
    return word

asking_to_play_game()

# 2. Display blank lines (in string?) for amount of letters in word that was selected 
# - 
# 3. If player guesses a correct letter, replace blank letter with line 
# -if letter is correct, put in place of line 
# 4. If player guesses wrong, make a tally mark or deduct from number of guesses
# -if letter not correct print letter below so player can see that they have already guesses that letter
# 5. Player wins if they guess the word
# -print "you win!"
# 6. Player loses if they run out of guesses
# -print "you lose!"



