
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
    def char_map(c):
        """
        Returns the ASCII value of a character.
        """
        return ord(c)

    message = ''.join([ord(c) - ord('A') + 2 for c in message])
    message = ''.join([chr(ord('A') + i) for i in message])
    return message

