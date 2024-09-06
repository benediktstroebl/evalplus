
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
    s = ''
    for i in message:
        if i in 'aeiou':
            if i in 'a':
                s += 'c'
            elif i in 'e':
                s += 'g'
            elif i in 'i':
                s += 'k'
            elif i in 'o':
                s += 's'
            elif i in 'u':
                s += 'v'
        else:
            s += i.upper() if i.islower() else i.lower()
    return s
