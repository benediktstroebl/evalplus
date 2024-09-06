
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
    vowels = 'aeiou'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    encoded = ''
    
    for i in message:
        if i in alpha:
            if i in vowels:
                ind = alpha.index(i)
                encoded += alpha[(ind+2)%26]
            else:
                ind = alpha.index(i)
                encoded += alpha[(ind+1)%26]
        else:
            encoded += i
    
    return encoded.swapcase()

