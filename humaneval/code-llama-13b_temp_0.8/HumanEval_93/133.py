
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
    result = ""
    for letter in message:
        if letter in "aeiouAEIOU":
            if letter.isupper():
                result += chr(ord(letter) + 2 - 65)
            else:
                result += chr(ord(letter) + 2 - 97)
        else:
            if letter.isupper():
                result += chr(ord(letter) - 65)
            else:
                result += chr(ord(letter) - 97)
    return result

