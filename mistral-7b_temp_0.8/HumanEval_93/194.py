
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
    """
    YOUR CODE HERE
    """
    if message == '':
        return ''

    vowels = 'aeiou'
    first_half = ''
    for letter in message:
        if letter in vowels:
            first_half += chr(ord(letter) + 2)
        elif letter.islower():
            first_half += chr(ord(letter) - 32)
        elif letter.isupper():
            first_half += chr(ord(letter) + 32)
    return first_half + encode(message[len(message) - len(first_half):])




