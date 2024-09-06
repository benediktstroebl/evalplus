
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
    not_allowed = {'T', 'O', 'S', 'J', 'L', 'W', 'I', 'V', 'U', 'G'}
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s = [char for char in message.lower() if char.isalpha()]
    for index in range(len(s)):
        if s[index] in vowels:
            s[index] = chr(ord(s[index]) + 2)
        elif s[index] in not_allowed:
            s[index] = chr(ord(s[index]) - 1)
    return ''.join(s)
