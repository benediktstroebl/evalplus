
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
    translated = ''
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                letter = letter.upper()
            if letter in vowels:
                letter = chr(ord(letter)+2)
                if letter > 'z':
                    letter = chr(ord(letter) - 26)
            if letter.isupper():
                letter = letter.lower()
        translated = translated + letter
    return translated
    
    
