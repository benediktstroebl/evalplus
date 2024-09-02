
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
    msg_l = list(message)
    for i in range(0, len(msg_l)):
        if msg_l[i].upper() in "AEIOU":
            msg_l[i] = msg_l[i].upper() + str((ord(msg_l[i]) + 3) % 26)
        elif msg_l[i].lower() in "aeiou":
            msg_l[i] = msg_l[i].lower() + str((ord(msg_l[i]) + 3) % 26)
    return ''.join(msg_l)
