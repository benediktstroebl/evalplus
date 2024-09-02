
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
    vowels = 'aeiou'
    encoded = ''
    for letter in message:
        if letter.lower() in vowels:
            # Vowels get encoded
            vowelIndex = vowels.index(letter.lower())
            encoded += vowels[(vowelIndex + 2) % len(vowels)]
        elif letter.isupper():
            # Uppercase letters get turned to lowercase
            encoded += letter.lower()
        else:
            # Lowercase letters get turned to uppercase
            encoded += letter.upper()
    return encoded
