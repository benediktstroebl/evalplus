
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
    message = message.upper()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    encoded = ''
    for char in message:
        index = char.lower() - 65
        if index in range(0, 25):
            encoded += letters[index]
        elif index in range(25, 27):
            encoded += letters[index - 26]
        else:
            encoded += letters[index - 25]
    return encoded
