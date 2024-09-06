
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
    new_message = ''
    for char in message:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
                char = chr(ord(char) + 13)
            else:
                char = char.upper()
                char = chr(ord(char) + 13)
        new_message += char
    return new_message

