
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    # -----------------------------------
    # CSC148 Fall 2016
    # Homework 2 - Othello
    #
    # Comment from Homework 1:
    #
    # The main functionality of your game is implemented in the 
    # function "play_game", you should not change this function.
    # Your "computer" implementation can be found in the file "computer_ai.py".
    # Your "human" implementation can be found in the file "human_player.py".
    # You need to implement the function "play_game" and 
    # your "computer" and "human" implementations, 
    # and you need to complete the code in "computer_ai.py" and "human_player.py".
    #
    # -----------------------------------
    
    # your code goes here
    if re.search(" +" ,text) :
        while re.search(" +" ,text):
            text = re.sub(' +','_',text)
    text = re.sub('_+','_',text)
    return text
