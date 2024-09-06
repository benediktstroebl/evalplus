
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
    # substitute vowels with letters 2 places ahead of them
    message = message.lower()
    swapped_message = []
    for char in message:
        if char in VOWELS:
            swapped_message.append(swap_letters(char))
        else:
            swapped_message.append(char)
    swapped_message = ''.join(swapped_message)
    return swapped_message
