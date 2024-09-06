
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
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for i in message:
        if i.lower() in vowels:
            result += vowels[(vowels.index(i.lower()) + 2) % len(vowels)]
        else:
            result += i.lower()
    return result
