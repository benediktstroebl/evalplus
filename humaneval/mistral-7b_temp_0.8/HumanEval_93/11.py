
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
        if char.isalpha():
            if char.islower():
                encoded += char.upper()
            else:
                encoded += char.lower()
        else:
            encoded += char
    for vowel in vowels:
        for char in message:
            if char == vowel:
                if char.isalpha():
                    if char.islower():
                        encoded += chr(ord(vowel) + 2)
                    else:
                        encoded += chr(ord(vowel.upper()) + 2)
                    break
    return encoded
