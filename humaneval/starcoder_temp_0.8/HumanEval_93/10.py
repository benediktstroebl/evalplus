
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
    
    # make sure that the message is a string
    if not isinstance(message, str):
        raise TypeError('message must be a string')
    
    # if the message is empty, return empty string
    if not message:
        return ''
    
    # make a copy of message to return
    output = message[:]
    
    # convert message to list of upper case letters
    message = list(message.upper())
    
    # iterate through message and swap case
    for i in range(len(message)):
        # if the letter is a vowel, find letter that comes 2 places 
        # ahead in the alphabet and swap it
        if message[i] in 'AEIOU':
            j = i + 2
            # if the second letter is outside the alphabet, just swap
            # the first letter
            if j > 26:
                j = i
            output = output[:i] + output[i:j][::-1] + output[j:]
    
    return output
