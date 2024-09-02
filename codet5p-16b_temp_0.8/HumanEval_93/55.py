
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

    letters = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'

    code = ''
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                code += letters[letters.find(letter.lower()) + 2].upper()
            else:
                code += letters[letters.find(letter) + 2]
        else:
            code += letter

    return code
