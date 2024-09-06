
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

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_index = []
    encoded = ''
    
    for index in range(len(message)):
        if message[index] in vowels:
            vowel_index.append(index)
    
    for index in vowel_index:
        encoded += message[index].upper()
        
    for index in range(len(message)):
        if message[index] in vowels:
            encoded += message[index + 2]
        else:
            encoded += message[index].lower()
    
    return encoded

