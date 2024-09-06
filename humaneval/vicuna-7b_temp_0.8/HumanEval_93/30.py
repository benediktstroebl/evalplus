
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
    message = message.translate(str.maketrans('', '', string.punctuation))
    message = ''.join([c for c in message if c.isalpha()])
    return message.replace('a', '2a').replace('b', '2b').replace('c', '2c').replace('d', '2d').replace('e', '2e').replace('f', '2f').replace('g', '2g').replace('h', '2h').replace('i', '2i').replace('l', '2l').replace('n', '2n').replace('o', '2o').replace('p', '2p').replace('r', '2r').replace('s', '2s').replace('t', '2t').replace('u', '2u').replace('w', '2w').replace('y', '2y')
