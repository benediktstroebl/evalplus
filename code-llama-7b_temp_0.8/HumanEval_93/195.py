
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
    message = message.replace('a', '2').replace('e', '3')
    message = message.replace('i', '4').replace('o', '5')
    message = message.replace('u', '6').replace('A', '2').replace('E', '3')
    message = message.replace('I', '4').replace('O', '5').replace('U', '6')
    message = message.replace('2', 'E').replace('3', 'I').replace('4', 'O')
    message = message.replace('5', 'U').replace('6', 'A')
    message = message.replace('1', 'A').replace('2', 'B').replace('3', 'C')
    message = message.replace('4', 'D').replace('5', 'E').replace('6', 'F')
    message = message.replace('7', 'G').replace('8', 'H').replace('9', 'I')
    message = message.replace('0', 'J').replace('1', 'K').replace('2', 'L')
    message = message.replace('3', 'M').replace('4', 'N').replace('5', 'O')
    message = message.replace('6', 'P').replace('7', 'Q').replace('8', 'R')
    message = message.replace('9', 'S').replace('0', 'T').replace('1', 'U')
    message = message.replace('2', 'V').replace('3', 'W').replace('4', 'X')
    message = message.replace('5', 'Y').replace('6', 'Z').replace('7', 'A')
    message = message.replace('8', 'B').replace('9', 'C').replace('0', 'D')
    return message
