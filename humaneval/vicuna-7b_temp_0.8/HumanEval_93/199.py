
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
    # convert message to lowercase
    message = message.lower()
    
    # create a dictionary to map vowels to their position in the alphabet
    vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    alphabet = ''.join([chr(i) for i in range(65, 92)]) + 'z'
    map(lambda x: alphabet[vowels[x]], vowels)
    
    # loop through the message and replace vowels with the corresponding mapped symbol
    result = ''
    for char in message:
        if char in vowels:
            result += alphabet[vowels[char]]
        else:
            result += char
    return result
