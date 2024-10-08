
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
    message = message.lower()
    vowels = 'aeiou'
    output = ''
    for letter in message:
        if letter in vowels:
            index = vowels.index(letter)
            index_2_ahead = index + 2
            output += vowels[index_2_ahead]
        else:
            output += letter
    return output


