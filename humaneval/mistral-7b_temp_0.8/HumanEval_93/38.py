
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
    # YOUR CODE HERE
    if len(message)==0:
        return message
    else:
        # swap case
        message = message.swapcase()
        # replace vowels
        message = message.replace('a', 'c')
        message = message.replace('e', 'g')
        message = message.replace('i', 'k')
        message = message.replace('o', 'q')
        message = message.replace('u', 'w')
        # remove duplicates
        message = list(set(message))
        return ''.join(message)
