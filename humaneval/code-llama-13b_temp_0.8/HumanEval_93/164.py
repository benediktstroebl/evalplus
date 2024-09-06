
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
    message_encoded = ''
    
    # Swaps case of all letters
    message_encoded += message.swapcase()
    
    # Replaces all vowels in the message with the letter that 
    # appears 2 places ahead of that vowel in the english alphabet. 
    vowels = ('a', 'e', 'i', 'o', 'u')
    for letter in message_encoded:
        if letter in vowels:
            if letter == 'a':
                message_encoded = message_encoded.replace(letter, 'c', 1)
            elif letter == 'e':
                message_encoded = message_encoded.replace(letter, 'g', 1)
            elif letter == 'i':
                message_encoded = message_encoded.replace(letter, 'k', 1)
            elif letter == 'o':
                message_encoded = message_encoded.replace(letter, 's', 1)
            else:
                message_encoded = message_encoded.replace(letter, 't', 1)
                
    return message_encoded
