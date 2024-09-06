
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
    if len(message) < 1:
        return ''

    result = ''
    for letter in message:
        if letter.isalpha():
            if (ord(letter.lower()) - 96) % 2 == 0:
                result += letter.upper()
            else:
                result += letter.lower()
        else:
            result += letter
    return result
