
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    result = ''
    for char in message:
        if char.isalpha():
            upper = char.isupper()
            char = char.lower()
            if char in vowels:
                char = alphabet[(alphabet.index(char) + 2) % len(alphabet)]
            if upper:
                char = char.upper()
        result += char
    return result

