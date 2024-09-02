
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
    message = message.lower()
    # keep track of current position
    current_position = 0
    # build the result
    result = []
    for char in message:
        # if this is a vowel, replace it with the next vowel
        if char.isalpha() and char.islower() and char.isvowel():
            result.append(chr(ord('a') + current_position))
            current_position += 1
        else:
            result.append(char)
    return ''.join(result)
