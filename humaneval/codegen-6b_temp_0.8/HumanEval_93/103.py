
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
    vowels = {'a':'t', 'e':'t', 'i':'t', 'o':'t', 'u':'t'}
    
    new_message = ''
    for l in message:
        if l in vowels:
            k = vowels[l]
            new_message += k
        else:
            new_message += l

    return new_message
