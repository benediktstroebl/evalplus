
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
    
    for ch in message:
        if ch in 'aeiou':
            if ch == 'a':
                result += 'D'
            elif ch == 'e':
                result += 'F'
            elif ch == 'i':
                result += 'H'
            elif ch == 'o':
                result += 'J'
            elif ch == 'u':
                result += 'N'
        else:
            if ch.islower():
                result += ch.upper()
            else:
                result += ch.lower()

    return result


