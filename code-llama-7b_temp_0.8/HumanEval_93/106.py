
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

    # find the code for all letters
    letter_code = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0, 26):
        letter_code[alphabet[i]] = alphabet[i + 2]

    encoded_message = ''
    for char in message:
        if char.lower() in letter_code:
            encoded_message += letter_code[char.lower()].upper()
        else:
            encoded_message += char
    return encoded_message

