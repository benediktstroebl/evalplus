
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
    # example for base case
    if len(message) == 0:
        return message
    
    # base case for checking if message has only one char
    if len(message) == 1:
        return message[0]
    
    # split message into a list of characters
    message_list = message.split()
    
    # iterate through each character
    for i, c in enumerate(message_list):
        if c.isalpha():
            # replace vowels with new vowels
            if c.islower():
                new_c = ''.join(['{}{}'.format(i+2, c) for i in range(ord(c) - 1)])
            elif c.isupper():
                new_c = ''.join(['{}{}'.format(i+2, c[1]) for i in range(ord(c[1]) - 1)])
            else:
                new_c = ''.join(['{}{}'.format(ord(c) - 1, c[1]) for i in range(ord(c) - 1)])
            message_list[i] = new_c
    
    return ''.join(message_list)