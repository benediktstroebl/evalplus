
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
    message = ''.join([i - 2 if i.isalpha() and i.isupper() else i for i in message])  # convert to all lowercase
    message = ''.join([c[1] for c in message])  # swap case of all letters
    message = message.translate(str.maketrans('aeiou', 'Aeiou'))  # replace vowels
    return message
