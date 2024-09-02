
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
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # encuentra todas las vocales
    message = [i for i in message if i in vowels]
    for i in message:
        for j in alpha:
            if j == i:
                new_alpha = alpha[alpha.index(i) - 2]
    return new_alpha


