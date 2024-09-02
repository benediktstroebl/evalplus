
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

    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for c in message:
        if c.islower():
            c = c.upper()
        elif c.isupper():
            c = c.lower()
        if c in vowels:
            index = vowels.index(c)
            c = vowels[(index + 2) % 5]
        result += c
    return result
    
