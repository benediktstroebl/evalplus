
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
    def swap(c):
        if c.isupper():
            return c.lower()
        else:
            return c.upper()

    def replace(c):
        if c in 'aeiouAEIOU':
            return chr(ord(c) + 2)
        return c

    return ''.join(map(swap, message))

