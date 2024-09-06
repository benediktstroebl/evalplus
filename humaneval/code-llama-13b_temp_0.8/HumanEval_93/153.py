
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
    message = message.swapcase()
    message = message.replace('a', 'c').replace('e', 'g').replace('i', 'j').replace('o', 'p').replace('u', 'x')
    message = message.replace('A', 'C').replace('E', 'G').replace('I', 'J').replace('O', 'P').replace('U', 'X')
    message = message.replace('c', 'a').replace('g', 'e').replace('j', 'i').replace('p', 'o').replace('x', 'u')
    message = message.replace('C', 'A').replace('G', 'E').replace('J', 'I').replace('P', 'O').replace('X', 'U')
    return message
