
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_message = ''
    for char in message:
        if char in vowels:
            char_index = vowels.index(char)
            new_message += vowels[(char_index + 2) % 5]
        else:
            new_message += char
    return new_message



