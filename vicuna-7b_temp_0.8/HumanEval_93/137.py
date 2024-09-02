
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
    message = message.upper()
    # Step 1: Swap case of all letters
    message = message.swapcase()
    
    # Step 2: Replace vowels with the letter that appears 2 places ahead of that vowel in the english alphabet.
    #         The vowels are: 'a', 'e', 'i', 'o', 'u'
    vowels = 'aeiouAEIOU'
    message = message.replace(vowels, vowels[vowels.index(message[vowels.index(message.lower())])+2])
    
    return message
