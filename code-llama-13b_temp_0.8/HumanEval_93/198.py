
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
    encoded = ''
    vowels = 'aeiou'
    new_vowels = vowels[2:] + vowels[:2]
    for char in message:
        if char.islower():
            char = char.upper()
        if char.lower() in vowels:
            char = new_vowels[vowels.index(char.lower())]
        encoded += char
    return encoded
