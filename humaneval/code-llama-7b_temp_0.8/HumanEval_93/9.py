
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
    
    # encode function encoded message and return the encoded message
    def encode(message):
        encoded_message = ""
        for character in message:
            if character.isalpha():
                if character.islower():
                    encoded_message += character.upper()
                elif character.isupper():
                    encoded_message += character.lower()
            elif character.isupper():
                encoded_message += chr(ord(character) + 2)
            else:
                encoded_message += character
        return encoded_message
    return encode(message)

