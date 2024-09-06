
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
    encoder = ''
    for i in range(0, len(message)):
        if message[i] == 'a':
            encoder += 'A'
        elif message[i] == 'e':
            encoder += 'E'
        elif message[i] == 'i':
            encoder += 'I'
        elif message[i] == 'o':
            encoder += 'O'
        elif message[i] == 'u':
            encoder += 'U'
        elif message[i] == 'A':
            encoder += 'a'
        elif message[i] == 'E':
            encoder += 'e'
        elif message[i] == 'I':
            encoder += 'i'
        elif message[i] == 'O':
            encoder += 'o'
        elif message[i] == 'U':
            encoder += 'u'
        elif message[i] == ' ':
            encoder += ' '
        else:
            if message[i].isupper():
                encoder += chr(ord(message[i]) + 2)
            else:
                encoder += chr(ord(message[i]) - 2)
    return encoder


