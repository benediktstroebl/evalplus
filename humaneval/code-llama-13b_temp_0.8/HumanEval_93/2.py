
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
    vowels = 'AEIOU'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
            if char in vowels:
                char = chr(ord(char) + 2)
                if char.isalpha():
                    char = char.upper()
            else:
                char = char.upper()
        new_message += char
    return new_message
