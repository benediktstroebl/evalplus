
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

    
    swapped_message = message.swapcase()
    vowels = ('a', 'e', 'i', 'o', 'u')
    encoded_message = ""

    for i in swapped_message:
        if i in vowels:
            encoded_message += (swapped_message[swapped_message.index(i) + 2])
        else:
            encoded_message += (swapped_message[swapped_message.index(i)])

    return encoded_message
