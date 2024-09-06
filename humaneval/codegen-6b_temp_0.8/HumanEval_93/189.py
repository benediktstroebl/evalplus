
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
    vowels = [l for l in 'aeiouAEIOU']
    encoded_message = ''
    for letter in message:
        if letter in vowels:
            index = vowels.index(letter)
            encoded_message += vowels[index + 2]
        else:
            encoded_message += letter
    return encoded_message
    
    