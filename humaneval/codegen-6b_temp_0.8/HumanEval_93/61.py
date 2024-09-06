
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
    
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    new_word = list(message)
    for i, letter in enumerate(message):
        if letter.lower() in vowels:
            if letter.isupper():
                new_word[i] = alpha[alpha.index(letter.lower()) + 2].upper()
            else:
                new_word[i] = alpha[alpha.index(letter.lower()) + 2]
    return ''.join(new_word)
