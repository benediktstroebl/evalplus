
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
    vowels = ['a','e','i','o','u']
    for char in message:
        char = char.lower()
        if char in vowels:
            vowel_index = vowels.index(char)
            next_vowel = vowels[(vowel_index + 2) % len(vowels)]
            encoded += next_vowel.upper()
        else:
            encoded += char.upper()
    return encoded
    
    
