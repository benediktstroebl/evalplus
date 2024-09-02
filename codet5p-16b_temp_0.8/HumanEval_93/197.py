
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
    encoded = ""
    for char in message:
        if char in vowels:
            encoded = encoded + char + message[message.find(char) + 2]
        else:
            encoded = encoded + char
    return encoded.swapcase()
