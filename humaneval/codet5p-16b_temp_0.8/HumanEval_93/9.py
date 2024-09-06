
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

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    encoded_message = ''
    
    for letter in message:
        if letter.lower() in vowels:
            encoded_message += alphabet[(alphabet.find(letter.lower()) + 2) % 26].upper()
        else:
            encoded_message += alphabet[alphabet.find(letter.lower())]
        
    return encoded_message

