
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
    vowels = 'aeiou'
    encoding_dict = {'a':'c', 'e':'g', 'i':'k', 'o':'s', 'u':'v',
                     'A':'C', 'E':'G', 'I':'K', 'O':'S', 'U':'V'}
    new_message = ''
    for character in message:
        if character in encoding_dict:
            new_message += encoding_dict[character]
        elif character in vowels:
            new_message += chr(ord(character)+2)
        else:
            new_message += character
    return new_message
