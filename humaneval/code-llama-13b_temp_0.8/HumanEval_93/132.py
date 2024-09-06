
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
    vowels = 'aeiou'
    encoded_message = ''
    for letter in message:
        if letter.lower() in vowels:
            next_vowel = vowels.index(letter.lower()) + 2
            if next_vowel >= len(vowels):
                next_vowel = 0
            letter = vowels[next_vowel]
        encoded_message += letter.swapcase()
    return encoded_message
