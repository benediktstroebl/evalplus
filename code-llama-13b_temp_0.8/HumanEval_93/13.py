
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
    
    def shift(letter):
        """
        A function to return the letter 2 places ahead of the letter
        given.
        """
        letter = letter.lower()
        if letter in "aeiou":
            return chr(ord(letter) + 2)
        else:
            return letter
    return ''.join([shift(char) for char in message])
        






