
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
    encode_msg = ""
    for char in message:
        if char in "aeiou":
            encode_msg += chr(ord('a') + ((ord(char) - ord('a') + 2) % 26))
        else:
            encode_msg += char
    return encode_msg
