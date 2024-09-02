
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
    message_list = list(message)
    for i in range(len(message_list)):
        if message_list[i].isalpha():
            if message_list[i] in CPL:
                message_list[i] = CPL[PL.index(message_list[i]) + 2]
            elif message_list[i] in RPL:
                message_list[i] = RPL[PL.index(message_list[i]) - 2]
    return ''.join(message_list)

