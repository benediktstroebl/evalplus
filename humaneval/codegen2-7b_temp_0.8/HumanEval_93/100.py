
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
    
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded_message = []
    
    for letter in message.lower():
        position = letters.find(letter)
        position += 2
        encoded_message.append(letters[position])
    
    return ''.join(encoded_message)
