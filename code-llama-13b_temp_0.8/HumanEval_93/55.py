
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
    vowels_list = list(vowels)
    encoded_message = ''
    for char in message:
        if char.isupper():
            char = char.lower()
        if char in vowels:
            index = vowels_list.index(char)
            encoded_char = vowels_list[index+2]
        else:
            encoded_char = char
        encoded_message += encoded_char
    return encoded_message.upper()
    
    
    
