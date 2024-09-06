
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
    vowels_2_ahead = dict(zip(vowels, vowels[2:] + vowels[:2]))
    encoded_message = []
    for char in message:
        if char.isupper():
            encoded_message.append(vowels_2_ahead.get(char.lower(), char).upper())
        else:
            encoded_message.append(vowels_2_ahead.get(char, char))
    return ''.join(encoded_message)
            
            
