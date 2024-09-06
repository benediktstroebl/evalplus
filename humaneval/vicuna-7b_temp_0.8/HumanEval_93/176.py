
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
    message = message.upper()
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.isalpha() and (char.isupper() and char != 'A'):
                index = ord(char) - 1
                encoded_char = chr(index + 2)
                encoded_message = encoded_message + encoded_char
            else:
                encoded_char = char
        else:
            encoded_char = chr(ord(char) - 1)
        encoded_message = encoded_message + encoded_char
    return encoded_message

