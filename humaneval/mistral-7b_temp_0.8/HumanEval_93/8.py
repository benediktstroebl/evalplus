
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
    for i in message:
        if i == 'A':
            print('C')
        elif i == 'B':
            print('D')
        elif i == 'C':
            print('E')
        elif i == 'D':
            print('F')
        elif i == 'E':
            print('G')
        elif i == 'F':
            print('H')
        elif i == 'G':
            print('I')
        elif i == 'H':
            print('J')
        elif i == 'I':
            print('K')
        elif i == 'J':
            print('L')
        elif i == 'K':
            print('M')
        elif i == 'L':
            print('N')
        elif i == 'M':
            print('O')
        elif i == 'N':
            print('P')
        elif i == 'O':
            print('Q')
        elif i == 'P':
            print('R')
        elif i == 'Q':
            print('S')
        elif i
