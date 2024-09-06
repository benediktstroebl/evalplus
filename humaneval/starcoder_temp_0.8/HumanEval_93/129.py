
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
            (
                (
                    'z' * (ord(letter) - ord('a')) +
                    'a' * (26 - (ord(letter) - ord('a')) - 1)
                )[0]
            )
            if letter.lower() in 'aeiou'
            else letter.upper()
            for letter in message
        ]
    )

