
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

    
    vowels = 'AEIOUaeiou'
    
    lower = message.lower()
    upper = message.upper()
    
    encoded_message = ''
    for c in lower:
        if c in vowels:
            index = vowels.find(c)
            new_letter = vowels[(index+2)%len(vowels)]
            encoded_message += new_letter
        else:
            encoded_message += c
            
    for c in upper:
        if c in vowels:
            index = vowels.find(c)
            new_letter = vowels[(index+2)%len(vowels)]
            encoded_message += new_letter
        else:
            encoded_message += c
            
    return encoded_message
        
