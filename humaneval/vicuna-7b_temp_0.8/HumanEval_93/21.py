
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
    # create a dictionary to map each letter to its position in the alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = {}
    for i in range(len(alphabet)):
        mapping[alphabet[i]] = i
    
    # encode the message
    encoded_message = ""
    for character in message:
        # swap the case
        if character.isupper():
            encoded_character = character.lower()
        else:
            encoded_character = character.upper()
        # replace vowels with their positions
        for i, vowel in enumerate(encoded_character):
            if vowel in mapping:
                encoded_character = encoded_character[:i] + mapping[vowel] + encoded_character[i+1:]
        # add the encoded character to the encoded message
        encoded_message += encoded_character
    return encoded_message
