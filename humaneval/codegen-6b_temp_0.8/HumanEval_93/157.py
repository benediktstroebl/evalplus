
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
    
    
    
    # find vowels, put into dictionary
    vowel_dict = {}
    for index, value in enumerate(string.ascii_lowercase):
        vowel_dict[value] = ''.join(string.ascii_lowercase[(index+2)%26:index] + string.ascii_lowercase[index+1:index] + string.ascii_lowercase[index+2:index+2])
    
    # replace vowels
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        message = message.replace(vowel, vowel_dict[vowel])
    
    return message
    
    
    