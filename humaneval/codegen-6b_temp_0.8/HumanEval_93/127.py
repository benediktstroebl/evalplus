
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
    # a = 'abcdefghijklmnopqrstuvwxyz'
    # for i, j in enumerate(a):
    #     if j in 'aeiou':
    #         a[i] = a[(i+2)%26]
    return (''.join(a if not j in 'aeiou' else j if not j.isupper() else j.swapcase() for j in message))

