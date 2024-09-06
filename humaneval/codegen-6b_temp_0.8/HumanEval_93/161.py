
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
    
    
    vowels = 'aeiouAEIOU'
    end = len(message)
    begin = 0
    message = message.lower()
    
    while begin < end:
        if message[begin] in vowels:
            letter = message[begin]
            message = message[:begin] + message[begin+2:]
            message = message[:begin] + letter + message[begin+1:]
            begin += 1
        else:
            begin += 1
    return message
    