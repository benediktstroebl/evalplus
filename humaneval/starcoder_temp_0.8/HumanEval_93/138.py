
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_new = ''
    
    for char in message:
        if char.lower() in alphabet:
            if char.lower() in 'aeiou':
                index = alphabet.find(char.lower())
                message_new += alphabet[index + 2]
            else:
                message_new += char.lower()
        else:
            message_new += char
    return message_new
