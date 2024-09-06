
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
    #replace all vowels with the letter that appears 2 places ahead of that vowel
    encoded = re.sub('[AEIOU]', lambda x: chr(ord(x.group(0)) + 2), message)
    
    #swap all letters' case
    encoded = encoded.swapcase()
    
    return encoded

