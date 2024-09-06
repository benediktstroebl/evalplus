
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
    
    trans = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 'cdefghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC')
    trans2 = str.maketrans("aeiouAEIOU", "cdefghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC")
    trans3 = str.maketrans("aeiouAEIOU", "cdefghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC")
    trans4 = str.maketrans("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ", "BCDEFGHIJKLMNOPQRSTUVWXYZbcdfghjklmnpqrstvwxyz")
    trans5 = str.maketrans("cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "cdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    message = message.translate(trans).translate(trans2).translate(trans3).translate(trans4).translate(trans5)
    return message

