
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
    message = list(message)
    vowels = 'aeiouAEIOU'
    for i, char in enumerate(message):
        if char in vowels[1:]:
            j = vowels.find(char)
            message[i] = vowels[j+1]
            message[i+1] = vowels[j]
    return ''.join(message)
