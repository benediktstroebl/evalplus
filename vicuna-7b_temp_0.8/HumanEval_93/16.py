
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
    encoded_message = []
    for char in message:
        # Replace vowels with the 2nd letter of their alphabet position
        if char in 'aeiouAEIOU':
            new_char = alphabet[ord(char) - ord('A') + 2]
            encoded_message.append(new_char)
        else:
            encoded_message.append(char)
    return encoded_message
