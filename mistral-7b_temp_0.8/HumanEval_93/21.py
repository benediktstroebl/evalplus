
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # your code here
    message = message.lower()
    encoded = ""

    for letter in message:
        if letter.isalpha():
            if letter == "a":
                encoded += "c"
            elif letter == "b":
                encoded += "d"
            elif letter == "c":
                encoded += "e"
            elif letter == "d":
                encoded += "f"
            elif letter == "e":
                encoded += "g"
            elif letter == "f":
                encoded += "h"
            elif letter == "g":
                encoded += "i"
            elif letter == "h":
                encoded += "j"
            elif letter == "i":
                encoded += "k"
            elif letter == "j":
                encoded += "l"
            elif letter == "k":
                encoded += "m"
            elif letter == "l":
                encoded += "n"
            elif letter == "m":
                encoded += "o"
            elif letter == "n":
                encoded += "
