
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
    
    letters = [c for c in message]
    encoded = []
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    # swaps case of all letters in message
    for c in letters:
        if c.isupper():
            encoded.append(c.lower())
        else:
            encoded.append(c.upper())
    
    # replace vowels in message with letters 2 places ahead of vowel in alphabet
    for i in range(len(encoded)):
        if encoded[i] in vowels:
            index = (ord(encoded[i]) - ord('a') + 2) % 26 + ord('a')
            encoded[i] = chr(index)
    return ''.join(encoded)
            
            
