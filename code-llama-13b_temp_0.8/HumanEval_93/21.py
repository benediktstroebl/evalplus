
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
    
    # your code here
    message = message.swapcase()
    new_string = ''
    for x in message:
        if x in 'aeiouAEIOU':
            vowel_location = 'aeiou'.find(x.lower())
            new_string += 'aeiou'[vowel_location+2]
        else:
            new_string += x
    return new_string
