
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

    # use a regular expression to match all the vowels
    vowels = r"[aeiou]"

    # use a regular expression to match all the consonants
    consonants = r"[bcdfghjklmnpqrstvwxz]"

    # swap case of all letters
    message = message.upper()

    # replace all vowels with next letter
    for letter in message:
        if letter in vowels:
            message = message.replace(letter, chr(ord(letter) + 2))

    return message

