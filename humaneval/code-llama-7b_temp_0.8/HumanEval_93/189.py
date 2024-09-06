
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
    vowels = 'AEIOUaeiou'
    enc_msg = []
    for char in message:
        if char in vowels:
            enc_msg.append(char)
        else:
            if char.isupper():
                enc_msg.append(chr(ord(char)+2))
            else:
                enc_msg.append(chr(ord(char)-2))
    return ''.join(enc_msg)
