
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded = ''
    for char in message:
        char_upper = char.upper()
        if char in vowels:
            index = (vowels.index(char) + 2) % len(vowels)
            char = vowels[index]
        encoded += char if char_upper == char else char.lower()
    return encoded

