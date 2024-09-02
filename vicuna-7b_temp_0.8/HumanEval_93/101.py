
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
    message = message.upper() # convert message to uppercase
    message = message.translate(str.maketrans('', '', string.punctuation)) # remove punctuation
    # iterate over the characters in the message
    for char in message:
        if char.isalpha():
            # if the character is an alphabetical character
            # swap the case of the character
            char = chr(ord(char) ^ ord('a'))
        elif char.isdigit():
            # if the character is a digit
            # replace the character with itself
            char = char
    
    return message
