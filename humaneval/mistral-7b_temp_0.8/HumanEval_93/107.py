
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
    # TODO
    # First swap the case of the letters
    # Replace the vowels
    result = []
    for letter in message:
        if letter.lower() in "aeiou":
            result.append(chr(ord(letter.lower())+2))
        else:
            result.append(letter.swapcase())
    return "".join(result)
