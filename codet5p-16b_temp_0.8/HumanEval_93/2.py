
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

    
    vowels = set('aeiou')
    
    encoded_message = []
    
    for letter in message:
        if letter.isupper():
            encoded_message.append(letter.lower())
        elif letter.lower() in vowels:
            encoded_message.append(chr(ord(letter) + 2))
        else:
            encoded_message.append(letter)
            
    return ''.join(encoded_message)
    
