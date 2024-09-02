
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
    import string
    alpha = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    alpha_vowels = 'aeiou'
    
    message = message.lower()
    alpha_lower = message.replace(alpha, alpha[::-1])
    vowels = alpha_lower.replace(alpha_vowels, alpha_vowels[2::-1])
    upper = vowels.upper()
    return upper

