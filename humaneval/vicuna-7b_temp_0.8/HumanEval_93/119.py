
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
    # Step 1: Swap case of all letters
    message = message.upper()
    
    # Step 2: Replace vowels with the letter 2 places ahead
    vowels = 'aeiouAEIOU'
    message = message.translate(vowels.upper().__getitem__((vowels.index(c)+2) % 5 for c in message))
    
    return message