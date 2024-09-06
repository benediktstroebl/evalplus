
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

    
    char_list = [letter.lower() for letter in message]
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded = []
    
    for char in char_list:
        if char in vowels:
            encoded.append(char_list[char_list.index(char) + 2])
        else:
            encoded.append(char_list[char_list.index(char)])
    
    encoded = ''.join(encoded)
    return encoded
    
