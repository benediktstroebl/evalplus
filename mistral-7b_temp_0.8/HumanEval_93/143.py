
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
    message_map = {}
    message_map['a'] = 'c'
    message_map['e'] = 'g'
    message_map['i'] = 'k'
    message_map['o'] = 'm'
    message_map['u'] = 's'
    encoded_message = ""
    for letter in message:
        if letter in message_map:
            encoded_message += message_map[letter]
        else:
            encoded_message += letter.swapcase()
    return encoded_message


