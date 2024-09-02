
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
    vowels_up = 'aeiou'
    cipher = ''
    for letter in message:
        if letter in vowels:
            index = vowels.find(letter)
            cipher += vowels[index + 2]
        elif letter in vowels_up:
            index = vowels_up.find(letter)
            cipher += vowels_up[index + 2]
        else:
            cipher += letter.upper()
    return cipher

