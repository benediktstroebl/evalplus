
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
    
    letter_index = {
        'a': 0, 
        'b': 1, 
        'c': 2, 
        'd': 3, 
        'e': 4, 
        'f': 5, 
        'g': 6, 
        'h': 7, 
        'i': 8, 
        'j': 9, 
        'k': 10, 
        'l': 11, 
        'm': 12, 
        'n': 13, 
        'o': 14, 
        'p': 15, 
        'q': 16, 
        'r': 17, 
        's': 18, 
        't': 19, 
        'u': 20, 
        'v': 21, 
        'w': 22, 
        'x': 23, 
        'y': 24, 
        'z': 25
    }
    
    message = message.lower()
    message = [letter_index[x] for x in message]
    
    vowels = [0, 4, 8, 12]
    
    for index in vowels:
        message[index], message[index + 2] = message[index + 2], message[index]
    
    return ''.join([chr(x) for x in message])
    
    



