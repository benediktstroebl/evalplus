
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

    new_message = message.swapcase()
    vowels = 'aeiouAEIOU'
    for char in new_message:
        if char in vowels:
            index = vowels.index(char)
            new_message = new_message.replace(char, vowels[index+2])
    return new_message
