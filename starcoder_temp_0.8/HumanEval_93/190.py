
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
    result = ""
    for i in message:
        if i == 'a':
            result += 'a'
        elif i == 'e':
            result += 'e'
        elif i == 'i':
            result += 'i'
        elif i == 'o':
            result += 'o'
        elif i == 'u':
            result += 'u'
        elif i == 'A':
            result += 'A'
        elif i == 'E':
            result += 'E'
        elif i == 'I':
            result += 'I'
        elif i == 'O':
            result += 'O'
        elif i == 'U':
            result += 'U'
        else:
            result += chr((ord(i) - 97 + 2) % 26 + 97)
    return result
