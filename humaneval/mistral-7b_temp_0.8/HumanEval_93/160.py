
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
    message_list = list(message)
    print(message_list)
    encode_dict = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'q',
        'u': 'y'
    }
    for index, item in enumerate(message_list):
        if item.islower():
            message_list[index] = item.upper()
        elif item.isupper():
            message_list[index] = item.lower()
        if item in encode_dict:
            message_list[index] = encode_dict[item]
    return ''.join(message_list)

