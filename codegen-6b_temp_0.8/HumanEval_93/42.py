
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
    dic = {'a': '0', 'e': '1', 'i': '2', 'o': '3', 'u': '4'}
    dic_upper = {'A': '0', 'E': '1', 'I': '2', 'O': '3', 'U': '4'}
    out = ''
    for char in message:
        if char is ' ':
            out += char
            continue
        if char.isalpha():
            out += dic[char.lower()]
        else:
            out += char
    return out

