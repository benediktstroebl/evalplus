
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
    new_alphabet = alphabet.upper()
    swapped_message = message.swapcase()
    encoded_message = ''
    for character in swapped_message:
        if character in alphabet:
            index = alphabet.index(character)
            encoded_message += new_alphabet[index]
        else:
            encoded_message += character
    return encoded_message

