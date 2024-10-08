
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
    return ''.join(
        [
            (''.join(
                [
                    str(letter[1].upper()) if letter[0] in VOWELS and letter[1] not in VOWELS else str(letter[1]) for letter in zip(message, message[1:] + message[0])
                ]
            ))
        ]
    )
