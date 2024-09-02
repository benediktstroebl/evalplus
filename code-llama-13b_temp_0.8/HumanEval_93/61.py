
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
    vowels = 'aeiouAEIOU'
    encoding = ''
    for letter in message:
        if letter in vowels:
            encoding += vowels[(vowels.index(letter) + 2) % len(vowels)]
        else:
            encoding += letter.lower() if letter.isupper() else letter.upper()
    return encoding




