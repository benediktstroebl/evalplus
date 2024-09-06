
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
    def encode_letter(letter):
        if letter == 'a':
            return '@'
        elif letter == 'e':
            return '3'
        elif letter == 'i':
            return '1'
        elif letter == 'o':
            return '0'
        elif letter == 'u':
            return '!'
        else:
            return letter
        
    def encode_string(message):
        encoded_message = ''
        for letter in message:
            encoded_message += encode_letter(letter)
        return encoded_message
    
    return encode_string(message)
