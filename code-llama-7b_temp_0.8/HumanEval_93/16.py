
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
    new_string = ""
    for letter in message:
        if letter.isupper():
            new_string += letter.lower()
        elif letter.islower():
            new_string += letter.upper()
        elif letter in 'aeiou':
            new_string += chr(ord(letter) + 2)
        else:
            new_string += letter
    return new_string

