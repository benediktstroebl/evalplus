
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

    
    message_encoded = ''
    for char in message:
        if char.isalpha():
            new_char = char.swapcase()
            if new_char in 'AEIOUaeiou':
                new_char = chr(ord(new_char)+2)
            message_encoded += new_char
        else:
            message_encoded += char
    return message_encoded
    
