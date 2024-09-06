
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
    return ''.join([
        letter.lower() if letter.lower() in vowels else letter.upper()
        if letter.isupper() else chr(ord(letter) - 2) if letter.lower() in vowels else letter
        for letter in message])

