
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
    def change_case(s):
        return ''.join([chr(ord('a') + i) for i in range(len(s))])
    
    message = message.lower()
    encoded = ''
    for char in message:
        if char.isalpha():
            encoded += change_case(char)
        else:
            encoded += char
    encoded = encoded.translate(str.maketrans('', '', string.punctuation))
    encoded = encoded.replace('a', 'z')
    encoded = encoded.replace('b', 'y')
    encoded = encoded.replace('c', 'x')
    encoded = encoded.replace('d', 'w')
    encoded = encoded.replace('e', 'v')
    encoded = encoded.replace('f', 'u')
    encoded = encoded.replace('g', 'p')
    encoded = encoded.replace('h', 'r')
    encoded = encoded.replace('i', 's')
    encoded = encoded.replace('j', 't')
    encoded = encoded.replace('k', 'q')
    encoded = encoded.replace('l', 'x')
    encoded = encoded.replace('m', 'v')
    encoded = encoded.replace('n', 'u')
    encoded = encoded.replace('o', 'r')
    encoded = encoded.replace('p', 'f')
    encoded = encoded.replace('q', 'w')
    encoded = encoded.replace('r', 'y')
    encoded = encoded.replace('s', 'v')
    encoded = encoded.replace('t', 'u')
    encoded = encoded.replace('u', 'y')
    encoded = encoded.replace('v', 'a')
    encoded = encoded.replace('w', 'c')
    encoded = encoded.replace('x', 'b')
    encoded = encoded.replace('y', 'd')
    encoded = encoded.replace('z', 'a')
    return encoded
