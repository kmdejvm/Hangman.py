import random 

def pick_a_word():
    """given a list of words, a word is selected at random""" 
    my_list = ['python', 'coding', 'change', 'computer', 'living']
    word = random.choice(my_list)
    return word 

def display_len_lines_in_word(word_to_guess):
    """display the blank lines in words set equal to length of word""" 
    for length in word_to_guess:
        print "_",
    print "\n"      

def pick_a_letter(num_correct_letters, word, word_progress):
    """picks a letter and determines whether the letter is in the word"""
    prompt = "\nPick any letter in the alphabet (a-z)\n>>>"
    letter = raw_input(prompt)
    num_of_occurrences = word.count(letter)
    start_search_index = 0
    if num_of_occurrences == 0:
        print "Sorry, that letter is not in the word" 
    else:
        for num in range(num_of_occurrences):    
            index = word.find(letter, start_search_index)
            word_progress[index] = letter
            start_search_index = index + 1
        return num_correct_letters + num_of_occurrences
    return num_correct_letters      

def guessing_word(word):
    """Asks player if they want to guess the word"""
    guess_word = raw_input ("Do you want to guess the word?: ") 
    if guess_word == "yes":
        final = raw_input ("Guess the word! ")         
        if final == word:
            print "Yes, the word was", word,"! Great job!"
        else:
            print "Sorry. The word was", word,". Better luck next time!"
        return True   
    else:
        return False              

def play_hangman():
    """Plays Hangman"""

    word = pick_a_word()
    word_progress = list(len(word) * "_")

    print "Your word is", str(len(word)), "characters long, guess a letter!"

    display_len_lines_in_word(word)
       
    num_correct_letters = 0
    guesses = 9
    guessed_letters = ""
    while True:
        num_correct_letters = pick_a_letter(num_correct_letters, word, word_progress)  
        print word_progress 
        if "_" not in word_progress:
            print "You have guessed the word"  
            break 
        if num_correct_letters > 2: 
            if guessing_word(word):
                break    
        if guesses >= 0:
            print "You have", guesses, "guesses left, choose wisely!"
            guesses = guesses - 1 
        if guesses <= 0:
            print "You only have 1 guess left or you lose!"              
                 
while True:
    play_again = raw_input ("Do you want to play Hangman? ")  
    if play_again == "yes" or "Yes":
        play_hangman()   
    else:
        print "Have a nice day! "
        break                    
     
    
        
           




    
   
       

        
         
          
        


    

        

