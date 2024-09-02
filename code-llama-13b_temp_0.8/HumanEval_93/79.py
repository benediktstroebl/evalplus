
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
    for character in message:
        if character.isupper():
            encoded_message += character.lower()
        else:
            encoded_message += character.upper()
    for character in encoded_message:
        if character in 'aeiouAEIOU':
            index = 'aeiou'.find(character) + 2
            if index > 5:
                index -= 5
            encoded_message = encoded_message.replace(character, 'aeiou'[index], 1)
    return encoded_message
