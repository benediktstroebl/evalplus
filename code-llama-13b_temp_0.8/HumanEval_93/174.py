
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
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Make a copy
    message = message.lower()
    
    # Encode
    message_encoded = ''
    for char in message:
        if char in vowels:
            message_encoded += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else:
            message_encoded += char
    return message_encoded.upper()
    
    
