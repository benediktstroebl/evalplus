
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
    for index, letter in enumerate(message):
        if letter.islower():
            message[index] = letter.upper()
        elif letter.isupper():
            message[index] = letter.lower()
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for index, letter in enumerate(message):
        if letter in vowels:
            message[index] = chr(ord(letter)+2)
            
    return message
