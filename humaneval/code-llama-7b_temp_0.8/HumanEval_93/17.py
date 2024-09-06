
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
    vowels_shifted = 'bcdfghjklmnpqrstvwxyz'
    msg = list(message)
    msg_shifted = []
    
    for char in msg:
        if char.lower() in vowels:
            index = vowels.find(char.lower())
            msg_shifted.append(vowels_shifted[index])
        else:
            if char.isupper():
                msg_shifted.append(char.lower())
            else:
                msg_shifted.append(char.upper())
    
    return ''.join(msg_shifted)
