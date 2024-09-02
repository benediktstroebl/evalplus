
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
    vowels = {'a':'y', 'e':'D', 'i':'d', 'o':'g', 'u':'c'}
    message_list = list(message)
    # Do not change this line (1)
    for i,character in enumerate(message_list):
        if character in vowels:
            char_pos = vowels[character]
            message_list[i] = chr(ord(message_list[i]) - ord(char_pos) + ord('a'))
    return ''.join(message_list)
