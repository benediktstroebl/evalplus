
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
    encoded_message = ""
    for i in range(len(message)):
        character = message[i]
        if character.isupper():
            character = character.lower()
        if character in 'aeiou':
            character = chr(ord(character) + 2)
        if character.islower():
            character = character.upper()
        encoded_message = encoded_message + character
    return encoded_message
