
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

    message_encoded = ""
    # get each letter from the string
    for letter in message:
        if letter.lower() in LETTERS:
            message_encoded += SWAP_TABLE[letter.lower()]
        else:
            message_encoded += letter

    return message_encoded
