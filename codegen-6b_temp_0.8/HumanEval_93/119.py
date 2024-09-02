
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
    encoded = ''
    for char in message:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or \
        char == 'u':
            encoded += char.lower()
        else:
            if ord(char) == 32:
                encoded += ' '
            else:
                encoded += char.lower()
    
    encoded = encoded.replace('ei', 'EI')
    encoded = encoded.replace('ea', 'EA')
    encoded = encoded.replace('ue', 'UE')
    encoded = encoded.replace('o', '0')
    encoded = encoded.replace('u', '0')
    
    print(encoded)
