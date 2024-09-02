
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
        if character.isalpha():
            if character.islower():
                encoded_character = character.upper()
            else:
                encoded_character = character.lower()

            if encoded_character in 'aeiou':
                encoded_character = chr((ord(encoded_character) + 2) % 26 + ord('a'))

            encoded_message += encoded_character
        else:
            encoded_message += character

    return encoded_message
