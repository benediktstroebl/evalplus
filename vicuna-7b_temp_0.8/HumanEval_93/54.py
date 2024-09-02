
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
    # initialize result with the message
    result = message
    for char in message:
        if char.isalpha():
            if char.isalpha():
                # swap positions of the two characters
                result = result[:i] + chr(ord(char) + 2) + result[i + 1:]
            elif char == "e":
                # replace "e" with "3"
                result = result[:i] + chr(ord("a") + 3) + result[i + 1:]
            elif char == "i":
                # replace "i" with "3"
                result = result[:i] + chr(ord("b") + 3) + result[i + 1:]
            elif char == "o":
                # replace "o" with "3"
                result = result[:i] + chr(ord("c") + 3) + result[i + 1:]
            elif char == "u":
                # replace "u" with "3"
                result = result[:i] + chr(ord("d") + 3) + result[i + 1:]
            else:
                # do nothing
                pass
    return result
