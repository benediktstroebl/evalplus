
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

    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    vowels = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'q',
        'u': 'w',
        'y': 'z'
    }
    vowels = {vowel: chr(ord(vowel) + 2) for vowel in vowels}

    message = list(message.lower())
    for i in range(len(message)):
        if message[i].lower() in vowels:
            message[i] = vowels[message[i]]
        else:
            message[i] = chr(ord(message[i]) ^ 32)
    message = ''.join(message)
    return message

