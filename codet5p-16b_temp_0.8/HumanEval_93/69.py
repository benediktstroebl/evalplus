
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

    assert type(message) == str, 'Message must be a string.'
    
    encoded_message = ''
    
    for char in message:
        if char.isalpha() == True:
            if char.isupper() == True:
                encoded_message += chr(ord(char) + 2).upper()
            else:
                encoded_message += chr(ord(char) + 2).lower()
        elif char.isalpha() == False:
            encoded_message += char
    
    return encoded_message
