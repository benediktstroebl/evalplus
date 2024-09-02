
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

    vowels = 'aeiou'
    new_message = ''
    for c in message:
        if c in vowels:
            new_message += vowels[(vowels.index(c) + 2) % 6]
        elif c.isupper():
            new_message += chr((ord(c) + 2 - 65) % 26 + 65)
        else:
            new_message += chr((ord(c) + 2 - 97) % 26 + 97)
    return new_message
