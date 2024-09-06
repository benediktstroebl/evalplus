
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
    import string
    alphabet = string.ascii_letters
    letters = map(lambda x: x.upper(), alphabet)
    pairs = zip(letters, letters[2:])
    shifted_letters = list(map(lambda x: x[1], pairs))+list(map(lambda x: x[0], pairs))
    return ''.join(map(lambda x: x if x in message else '', shifted_letters))
    
    
