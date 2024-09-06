
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
    message = message.upper()  # convert to uppercase
    encoded = ''
    for letter in message:
        if letter.isalpha():
            index = ord(letter) - 64  # 64 is the index of A
            if index >= 0 and index < 27:  # replace all vowels with two places ahead
                encoded += chr(index + 26)
            else:
                encoded += chr(index)
        else:
            encoded += chr(letter)
    return encoded
