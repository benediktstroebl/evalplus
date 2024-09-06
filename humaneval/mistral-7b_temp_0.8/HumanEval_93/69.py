
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
    m = list(message)
    for i in range(len(m)):
        if m[i].isalpha():
            if m[i].islower():
                m[i] = m[i].upper()
            else:
                m[i] = m[i].lower()
        elif m[i] == 'a':
            m[i] = 'c'
        elif m[i] == 'e':
            m[i] = 'g'
        elif m[i] == 'i':
            m[i] = 'k'
        elif m[i] == 'o':
            m[i] = 'q'
        elif m[i] == 'u':
            m[i] = 'w'
    return ''.join(m)

