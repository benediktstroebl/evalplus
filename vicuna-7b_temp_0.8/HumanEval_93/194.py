
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
    message = message.replace('a', '2')
    message = message.replace('b', '2')
    message = message.replace('c', '1')
    message = message.replace('d', '2')
    message = message.replace('e', '3')
    message = message.replace('f', '4')
    message = message.replace('g', '1')
    message = message.replace('h', '3')
    message = message.replace('i', '1')
    message = message.replace('i', '4')
    message = message.replace('j', '3')
    message = message.replace('k', '2')
    message = message.replace('l', '1')
    message = message.replace('m', '3')
    message = message.replace('n', '4')
    message = message.replace('o', '0')
    message = message.replace('p', '1')
    message = message.replace('q', '2')
    message = message.replace('r', '1')
    message = message.replace('s', '3')
    message = message.replace('t', '2')
    message = message.replace('u', '1')
    message = message.replace('v', '0')
    message = message.replace('w', '2')
    message = message.replace('x', '3')
    message = message.replace('y', '1')
    message = message.replace('z', '2')
    message = message.replace('1', 'a')
    message = message.replace('2', 'b')
    message = message.replace('3', 'c')
    message = message.replace('4', 'd')
    message = message.replace('5', 'e')
    message = message.replace('6', 'f')
    message = message.replace('7', 'g')
    message = message.replace('8', 'h')
    message = message.replace('9', 'i')
    return message
