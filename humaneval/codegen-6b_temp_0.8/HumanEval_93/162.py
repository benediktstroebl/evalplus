
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
    
    # If this is a lowercase message:
    if message == message.upper():

        # Check for vowels:
        for index, letter in enumerate(message):
            if letter in "AEIOUaeiou":
                vowel = message[index]
                message = message.replace(vowel, vowel + "2")

        # Encrypt the message:
        message = message.lower()
        encrypted = ""
        for index, letter in enumerate(message):
            encrypted += message[index - 2]
        return encrypted
    
    # If this is a uppercase message:
    else:

        # Check for vowels:
        for index, letter in enumerate(message):
            if letter in "AEIOUaeiou":
                vowel = message[index]
                message = message.replace(vowel, vowel + "2")

        # Encrypt the message:
        message = message.lower()
        encrypted = ""
        for index, letter in enumerate(message):
            encrypted += message[index - 2]
        return encrypted

import doctest
doctest.testmod()
