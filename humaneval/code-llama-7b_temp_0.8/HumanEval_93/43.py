
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
    # IMPLEMENTATION
    encoded_message = ''
    for character in message:
        if character in 'aeiou':
            if character.isupper():
                new_character = chr(ord(character) + 2)
            elif character.islower():
                new_character = chr(ord(character) - 2)
            else:
                print("Invalid character")
                return None
            encoded_message += new_character
        else:
            encoded_message += character.swapcase()
    return encoded_message

