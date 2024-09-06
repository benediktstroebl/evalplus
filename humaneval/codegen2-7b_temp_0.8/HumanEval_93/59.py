
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
    return message.replace('e', '3').replace('a', '4').replace('i', '1').replace('o', '0').replace('u', '2').replace('l', '5').replace('n', '6').replace('r', '7').replace('s', '8').replace('t', '9').replace('E', '3').replace('A', '4').replace('I', '1').replace('O', '0').replace('U', '2').replace('L', '5').replace('N', '6').replace('R', '7').replace('S', '8
