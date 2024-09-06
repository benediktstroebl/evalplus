
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
    result = ''
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char

    i = 0
    result2 = ''
    while i < len(result):
        if result[i] in 'AEIOU':
            result2 += chr(ord(result[i]) + 2)
            i += 1
        else:
            result2 += result[i]
            i += 1
    return result2
