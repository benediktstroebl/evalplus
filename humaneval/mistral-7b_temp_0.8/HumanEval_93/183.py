
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
    new_string = ''
    vowels = 'aeiou'
    for i in range(len(message)):
        if message[i] in vowels:
            if i < len(message) - 1:
                new_string += message[i + 2]
            else:
                new_string += message[0]
        else:
            new_string += message[i].upper() if message[i].islower() else message[i].lower()
    return new_string

