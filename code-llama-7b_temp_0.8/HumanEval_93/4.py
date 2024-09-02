
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
    message = message.lower()
    encoded_message = ""
    for char in message:
        if char.islower():
            if char == "a":
                encoded_message += "c"
            elif char == "e":
                encoded_message += "g"
            elif char == "i":
                encoded_message += "h"
            elif char == "o":
                encoded_message += "j"
            elif char == "u":
                encoded_message += "k"
            else:
                encoded_message += chr(ord(char) + 2)
        else:
            encoded_message += char

    return encoded_message

