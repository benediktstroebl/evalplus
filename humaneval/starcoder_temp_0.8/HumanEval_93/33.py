
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
    encoded_message = ''
    message = message.lower()
    vowels = ['a','e','i','o','u']
    for letter in message:
        if letter in vowels:
            letter = vowels[(vowels.index(letter) + 2) % 5]
        encoded_message += letter
    return encoded_message
