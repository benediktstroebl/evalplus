
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
    # convert message to lowercase
    message = message.lower()
    # step 1: encode message as base64
    encoded_message = base64.b64encode(message.encode('utf-8')).decode('utf-8')
    # step 2: swap case of letters in encoded message
    encoded_message = ''.join([c.upper() if c.isalpha() else c for c in encoded_message])
    # step 3: replace vowels with modified version
    modified_message = []
    for c in encoded_message:
        if c.isalpha():
            if c.isvowel():
                modified_message.append(chr(ord(c) + 2))
            else:
                modified_message.append(c)
    return ''.join(modified_message)
