
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
    m = message.upper()
    n = ""
    for i in range(len(m)):
        if m[i] in "AEIOU":
            n += m[i].upper()
        elif m[i] in "AEIOUY":
            n += m[i].upper()
        else:
            n += m[i]
    return
