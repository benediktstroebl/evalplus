
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
    def rotate(letter):
        if letter in 'aeiou':
            index = 'aeiou'.find(letter)
            new_letter = 'aeiou'[index + 2]
            return new_letter
        else:
            return letter.lower() if letter.isupper() else letter.upper()
    return ''.join([rotate(letter) for letter in message])
    
