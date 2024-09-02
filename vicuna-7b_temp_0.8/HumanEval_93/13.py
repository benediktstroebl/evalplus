
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
    message = message.upper()
    encoded = ""
    for char in message:
        if char.isalpha():
            index = ord(char) - 1
            if index >= 'A' and index <= 'Z':
                index += 26
            elif index >= 'a' and index <= 'z':
                index += 27
            if index >= 'A' and index <= 'Z':
                index += 26
            if index >= 'a' and index <= 'z':
                index += 27
            encoded += chr(index)
        else:
            encoded += char
    return encoded
