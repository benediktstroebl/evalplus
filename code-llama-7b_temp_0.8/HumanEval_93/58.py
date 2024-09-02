
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
    
    # replace all vowels in the message with the letter that 
    # appears 2 places ahead of that vowel in the english alphabet
    for vowel in 'AEIOUaeiou':
        message = message.replace(vowel, vowel[2])
    
    # swap case of all letters
    message = message.swapcase()
    
    return message


