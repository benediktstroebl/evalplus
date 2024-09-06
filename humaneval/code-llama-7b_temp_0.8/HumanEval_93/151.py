
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
    for c in message:
        if c.lower() in 'aeiou':
            result += chr(ord(c.lower())+2)
        elif c.isupper():
            result += c.lower()
        elif c.islower():
            result += c.upper()
        else:
            result += c
    return result

