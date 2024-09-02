
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
    message = ''.join(map(str, message))
    message = message.upper()  # change case to uppercase
    message = message.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    message = ''.join([''.join(c for c in letters if c in message) for letters in 'abcdefghijklmnopqrstuvwxyz'])  # remove letters
    message = message.translate(str.maketrans('', '', string.ascii_uppercase))  # change case to uppercase
    message = message.replace('a', 'A')
    message = message.replace('b', 'B')
    message = message.replace('c', 'C')
    message = message.replace('d', 'D')
    message = message.replace('e', 'E')
    message = message.replace('f', 'F')
    message = message.replace('g', 'G')
    message = message.replace('h', 'H')
    message = message.replace('i', 'I')
    message = message.replace('j', 'J')
    message = message.replace('k', 'K')
    message = message.replace('l', 'L')
    message = message.replace('m', 'M')
    message = message.replace('n', 'N')
    message = message.replace('o', 'O')
    message = message.replace('p', 'P')
    message = message.replace('q', 'Q')
    message = message.replace('r', 'R')
    message = message.replace('s', 'S')
    message = message.replace('t', 'T')
    message = message.replace('u', 'U')
    message = message.replace('v', 'V')
    message = message.replace('w', 'W')
    message = message.replace('x', 'X')
    message = message.replace('y', 'Y')
    message = message.replace('z', 'Z')
    message = message.replace('A', 'a')
    message = message.replace('B', 'b')
    message = message.replace('C', 'c')
    
