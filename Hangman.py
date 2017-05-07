import random 
# 1. Ask player if they want to play hangman?

def asking_to_play_game():
    """asks player if they want to play"""
    prompt = "\nDo you want to play Hangman with me, yes or no? \n>>>"
    yes_or_no = raw_input(prompt)
    if yes_or_no == "yes":
        print "Great!"
    else:
        print "Maybe we can play later!" 
        exit()

# 2. random selection of word 
def pick_a_word():
    """given a list of words, a word is selected""" 
    my_list = ['python', 'coding', 'change', 'living']
    word = random.choice(my_list)
    print word # print word # print word #keeping this in for trouble-shooting will remove for actual game
    return word

# 3. Display blank lines for amount of letters in word that was selected 
def display_len_lines_in_word(word_to_guess):
    """display the blank lines in words set equal to length of word"""
    
    for length in word_to_guess:
        print "_",
    print "\n"      

# 4. If player guesses a correct letter, replace blank letter with line 
def pick_a_letter():
    """given all the letters in the alphabet, the player is asked to pick any letter"""
    prompt = "\nPick any letter in the alphabet, a-z. \n>>>"
    letter = raw_input(prompt) 
    index = word.find(letter)
    
    if index == -1:
        print "That letter is not in the word"
    else:
       word_progress[index] = letter       
    
def display_incorrect_letters_guessed():
    """if letter is incorrect, display letter"""
    pass     

 
def guessing_correct_word():
    """if player guesses correct word before dashes are filled, they win!"""
    pass 

asking_to_play_game()
word = pick_a_word()
word_progress = list(len(word) * "_")

print "Your word is", str(len(word)), "characters long"
print word

display_len_lines_in_word(word)

while True:
    pick_a_letter() 
    print word_progress 
        


