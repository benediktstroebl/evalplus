
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
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    new_message = ''
    
    for letter in message:
        if letter not in vowels:
            if letter.isupper():
                new_message += letter.lower()
            else:
                new_message += letter.upper()
        else:
            new_message += chr((ord(letter) - ord('a') + 2) % 26 + ord('a'))
    
    return new_message
