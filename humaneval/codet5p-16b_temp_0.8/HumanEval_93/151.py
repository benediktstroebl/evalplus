
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

    vowels = ('a', 'e', 'i', 'o', 'u')
    swapped_message = ""
    for char in message.lower():
        if char in vowels:
            swapped_message += message[2:].index(char) * char
        else:
            swapped_message += char
    return swapped_message
