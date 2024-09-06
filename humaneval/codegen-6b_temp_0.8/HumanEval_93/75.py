
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
    from string import lowercase
    vowels = 'aeiou'
    new_message = ''
    for l in message.lower():
        if l in lowercase:
            idx = lowercase.index(l)
            if l in vowels:
                new_message += lowercase[idx + 2]
            else:
                new_message += lowercase[idx + 1]
        else:
            new_message += l
    return new_message

