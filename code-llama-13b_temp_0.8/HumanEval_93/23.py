
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
    vowels = "aeiouAEIOU"
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_dict = dict(zip(alpha, alpha[2:]+alpha[:2]))
    vowels_dict = dict(zip(vowels, alpha[2::2]+alpha[:2:2]))
    message = message.translate(str.maketrans(alpha_dict))
    message = message.translate(str.maketrans(vowels_dict))
    return message
