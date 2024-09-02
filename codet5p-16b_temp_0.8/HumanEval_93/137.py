
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
                new_message += char.lower()
                new_message += char.lower()
            else:
                new_message += char.upper()
                new_message += char.upper()
        else:
            new_message += char
    return new_message

