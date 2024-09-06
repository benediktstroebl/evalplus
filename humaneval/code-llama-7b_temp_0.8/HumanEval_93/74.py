
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
    vowels = "AEIOUaeiou"
    message = message.swapcase()
    new_msg = ""
    for i in message:
        if i in vowels:
            idx = vowels.index(i)
            i = vowels[(idx + 2) % 10]
        new_msg += i
    return new_msg
