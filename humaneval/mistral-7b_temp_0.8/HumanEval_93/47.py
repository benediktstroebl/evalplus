
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
    msg = message.upper()
    msg = ''.join([chr(ord(i) + 2) if i.lower() in 'aeiou' else i
                   for i in msg])
    msg = msg.replace('Q', 'K').replace('Z', 'Q')
    return msg

