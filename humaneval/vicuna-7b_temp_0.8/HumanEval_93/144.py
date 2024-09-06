
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
    if not isinstance(message, str):
        raise ValueError("Only strings are allowed")
    message = message.upper() # swap case
    vowels = 'aeiouAEIOU'
    result = []
    for char in message:
        if char in vowels:
            result.append(vowels.index(char)+2)
        else:
            result.append(char)
    return ''.join(result)
