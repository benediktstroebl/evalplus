
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
    letters = 'abcdefghijklmnopqrstuvwxyz'
    message = message.lower()
    
    def transform(letter):
        lindex = letters.find(letter)
        return letters[lindex+2]
    
    return "".join(map(transform, message))
