
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
    def shift_letter(letter):
        if letter.lower() in 'aeiou':
            return chr(ord(letter)+2 % 26 + 97)
        else:
            return letter.swapcase()
    return ''.join(map(shift_letter, message))
        
