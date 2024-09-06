
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
    message = message.upper()
    if 'a' in message:
        message = message.replace('a', 'z')
    elif 'e' in message:
        message = message.replace('e', 'a')
    elif 'i' in message:
        message = message.replace('i', 'u')
    elif 'o' in message:
        message = message.replace('o', 'i')
    elif 'u' in message:
        message = message.replace('u', 'o')
    for vowel in 'aeiou':
        if vowel in message:
            message = message.replace(vowel, str(ord(vowel)+1))
    return message
