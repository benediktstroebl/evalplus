
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

    msg = message.lower()
    for index in range(len(msg)):
        if msg[index] == 'a':
            msg = msg[:index] + 'a' + msg[index + 1:]
        if msg[index] == 'e':
            msg = msg[:index] + 'e' + msg[index + 1:]
        if msg[index] == 'i':
            msg = msg[:index] + 'i' + msg[index + 1:]
        if msg[index] == 'o':
            msg = msg[:index] + 'o' + msg[index + 1:]
        if msg[index] == 'u':
            msg = msg[:index] + 'u' + msg[index + 1:]
    return msg
