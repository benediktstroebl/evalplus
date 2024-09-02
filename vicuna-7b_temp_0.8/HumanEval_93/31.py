
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
    message = message.lower()
    encoded = []
    for char in message:
        if char.isalpha():
            idx = [idx + 2 for idx, char in enumerate(string.ascii_uppercase) if char == string.ascii_uppercase[idx]]
            encoded.append(char)
        else:
            encoded.append(char)
    return ''.join(encoded)