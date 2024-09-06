
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
    vowels = ['a','e','i','o','u']
    vowels_mapped = ['c','e','i','o','g']
    encoded = ''
    for c in message:
        if c.lower() in vowels:
            index = vowels.index(c.lower())
            encoded += vowels_mapped[index]
        else:
            encoded += c.swapcase()
    return encoded
            
        
            
        
        
        
    
