
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
    new_string = ''
    for letter in message:
        if letter in vowels:
            new_string += chr((ord(letter) + 2) % 26 + ord('a'))
        elif letter.isupper():
            new_string += letter.lower()
        else:
            new_string += letter.upper()
    return new_string
