
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
    encoded = ''
    
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                encoded += chr( ord(ch) + 2 - ord('A') )
            else:
                encoded += chr( ord(ch) + 2 - ord('a') )
        else:
            encoded += ch
            
    return encoded
    
