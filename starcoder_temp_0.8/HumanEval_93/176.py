
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
    # check if message is an ascii string
    if not isinstance(message, str):
        raise ValueError("message is not a string")
    message = message.upper()
    # check if message contains non-letter characters
    if not all(char.isalpha() for char in message):
        raise ValueError("message contains non-letters")
    # encode the message
    result = ''
    for letter in message:
        if letter in ALPHABET:
            # increment letter's index by 2 and wrap around to beginning
            if ALPHABET.index(letter) + 2 > 26:
                result += ALPHABET[ALPHABET.index(letter) + 2 - 26]
            else:
                result += ALPHABET[ALPHABET.index(letter) + 2]
        else:
            # no change for non-alphabetical characters
            result += letter
    return result
