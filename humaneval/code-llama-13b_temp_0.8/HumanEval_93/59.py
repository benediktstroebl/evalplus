
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
    message = list(message)
    for idx,letter in enumerate(message):
        if letter.isalpha():
            if letter.isupper():
                letter = letter.lower()
            if letter in vowels:
                if (vowels.index(letter)+2) < len(vowels):
                    message[idx] = vowels[vowels.index(letter)+2].upper()
                else:
                    message[idx] = vowels[2]
            message[idx] = letter.swapcase()
    return ''.join(message)
