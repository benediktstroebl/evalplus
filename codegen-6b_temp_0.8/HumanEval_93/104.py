
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
    punctuation = [' ', '.', '!', '?']
    vowels = ['A', 'E', 'I', 'O', 'U']
    translations = {'a': '2', 'e': '3', 'i': '!', 'o': '1', 'u': '$'}
    message = message.lower()
    for char in message:
        if char in punctuation:
            message = message.replace(char, '')
    translated = []
    for char in message:
        if char in vowels:
            translated.append(translations[char])
        else:
            translated.append(char)
    return ''.join(translated)
    
    