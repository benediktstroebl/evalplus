
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
    vowels = list(vowels)
    encoded_message = ''
    for letter in message:
        if letter.lower() in vowels:
            vowel_index = vowels.index(letter.lower())
            encoded_message += vowels[vowel_index+2]
        else:
            encoded_message += letter.lower() if letter.isupper() else letter.upper()
    return encoded_message
