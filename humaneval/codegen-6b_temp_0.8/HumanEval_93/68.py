
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
    import string
    vowels = 'aeiou'
    for letter in string.lowercase:
        message = message.replace(letter, letter.upper() if letter in vowels else \
        string.lowercase[(string.lowercase.index(letter) + 2) % 26])
    return message

