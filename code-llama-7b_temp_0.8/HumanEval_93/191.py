
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
    encoded_message = ""
    for char in message:
        if char.lower() in 'aeiou':
            new_char = chr((ord(char) + 2 - 97) % 26 + 97)
        else:
            new_char = char.upper() if char.islower() else char.lower()
        encoded_message += new_char
    return encoded_message

