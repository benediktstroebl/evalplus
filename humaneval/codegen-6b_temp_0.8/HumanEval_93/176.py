
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
    vowels = 'AEIOU'
    result = ''
    
    for i, char in enumerate(message):
        if char.isalpha():
            lower = char.lower()
            pos = vowels.find(lower)
            if pos == -1:
                result += message[i]
            else:
                result += message[i].upper() if pos + 2 > len(vowels) else message[i].upper()[pos + 2]
        else:
            result += char
    
    return result
