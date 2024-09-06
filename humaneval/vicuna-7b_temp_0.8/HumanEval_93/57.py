
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
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded_message = ''
    for char in message:
        # Check if char is a vowel
        if char in 'aeiou':
            # Replace with vowel 2 places ahead
            if char in alphabet[1:]:
                encoded_char = alphabet[1 + alphabet.index(char) % 26]
            else:
                encoded_char = char
        else:
            # Do nothing
            encoded_char = char
        encoded_message += encoded_char
    return encoded_message

