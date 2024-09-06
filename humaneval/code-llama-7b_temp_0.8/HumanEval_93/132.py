
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
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = alpha.upper()
    vowels = "aeiou"
    vowels_upper = vowels.upper()
    message = message.lower()
    encoded_message = ""
    
    for c in message:
        if c in vowels:
            ind = alpha.find(c)
            encoded_message += alpha_upper[ind+2]
        elif c in alpha:
            ind = alpha.find(c)
            encoded_message += alpha_upper[ind-2]
        else:
            encoded_message += c
    
    return encoded_message
