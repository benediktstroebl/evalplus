
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
    return ''.join([i.upper() if i.isupper() else i.lower() for i in message if i not in 'AEIOUaeiou' or i.upper() == 'Q']).replace('A', 'C').replace('B', 'D').replace('C', 'E').replace('D', 'F').replace('E', 'G').replace('F', 'H').replace('G', 'I').replace('H', 'J').replace('I', 'K').replace('J', 'L').replace('K', 'M').replace('L', 'N').replace('M', 'O').replace('N', 'P').replace('O', 'Q').replace('P', 'R').replace('Q', 'S').replace('R', 'T').replace('S', 'U').replace('T', 'V').replace('U', 'W').replace('V', 'X').replace('W', 'Y').replace('X', 'Z').replace('Z', 'A')
