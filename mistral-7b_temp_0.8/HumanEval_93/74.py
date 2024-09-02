
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
    #message_to_list = list(message)
    #message_to_list.reverse()
    #message = ''.join(message_to_list)
    #message = message.upper()
    #message = message.replace('A', 'C')
    #message = message.replace('E', 'G')
    #message = message.replace('I', 'K')
    #message = message.replace('O', 'Q')
    #message = message.replace('U', 'W')
    #message = message.replace('Y', 'A')
    #message = message.lower()
    #return message
    message = message.upper()
    message = message.replace('A', 'C')
    message = message.replace('E', 'G')
    message = message.replace('I', 'K')
    message = message.replace('O', 'Q')
    message = message.replace('U', 'W')
    message = message.replace('Y', 'A')
    message = message.lower()
    return message
