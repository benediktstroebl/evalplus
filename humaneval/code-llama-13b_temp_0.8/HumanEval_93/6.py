
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
    vowels_upper = 'AEIOU'
    new_message = ''
    
    for letter in message:
        if letter.lower() in vowels:
            new_message += vowels[(vowels.index(letter.lower())+2)%5]
        elif letter.lower() in vowels_upper:
            new_message += vowels_upper[(vowels_upper.index(letter.lower())+2)%5]
        else:
            new_message += letter
            
    return new_message
