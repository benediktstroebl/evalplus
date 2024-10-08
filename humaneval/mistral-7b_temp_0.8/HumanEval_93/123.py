
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
    result = ''
    for char in message:
        if char.isalpha():
            char = char.lower()
            if char in vowels:
                char = chr((ord(char) + 2) % 26 + ord('a'))
            if char.isupper():
                char = char.lower()
            else:
                char = char.upper()
            result += char
        else:
            result += char
    return result

