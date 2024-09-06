
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
    encoded_message = ''
    
    for char in message:
        if char.isupper():
            encoded_message += char.lower()
        else:
            encoded_message += char.upper()

    # Need to be encoded here since all chars are encoded.
    vowels = 'aeiou'
    encoded_vowels = 'qwrtz'
    vowels_map = dict(zip(vowels, encoded_vowels))

    encoded_message_with_vowels = ''
    for char in encoded_message:
        if char in vowels_map:
            encoded_message_with_vowels += vowels_map[char]
        else:
            encoded_message_with_vowels += char

    return encoded_message_with_vowels
    
    
