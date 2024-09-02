
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

    result = ''

    for char in message:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char

    result = result.replace('A', 'B')
    result = result.replace('B', 'A')
    result = result.replace('C', 'D')
    result = result.replace('D', 'C')
    result = result.replace('E', 'F')
    result = result.replace('F', 'E')
    result = result.replace('G', 'H')
    result = result.replace('H', 'G')
    result = result.replace('I', 'J')
    result = result.replace('J', 'I')
    result = result.replace('K', 'L')
    result = result.replace('L', 'K')
    result = result.replace('M', 'N')
    result = result.replace('N', 'M')
    result = result.replace('O', 'P')
    result = result.replace('P', 'O')
    result = result.replace('Q', 'R')
    result = result.replace('R', 'Q')
    result = result.replace('S', 'T')
    result = result.replace('T', 'S')
    result = result.replace('U', 'V')
    result = result.replace('V', 'U')
    result = result.replace('W', 'X')
    result = result.replace('X', 'W')
    result = result.replace('Y', 'Z')
    result = result.replace('Z', 'Y')

    return result
