
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

    # NOTE: this is not a good way to go about it. See the itertools solution below
    new_message = ''
    for char in message:
        # check if vowel
        if char in 'aeiou':
            # replace with char two places ahead
            new_message += chr(ord(char) + 2)
        else:
            # if not vowel, check if lowercase
            if char.islower():
                new_message += char.upper()
            else:
                new_message += char.lower()
    return new_message
    
