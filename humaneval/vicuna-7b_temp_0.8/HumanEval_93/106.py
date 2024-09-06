
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
        if letter.isupper():
            return letter.lower()
        elif letter.isalpha() and letter not in 'aeiouAEIOU':
            index = ord(letter) - ord('A') + 1
            return chr(index)
        else:
            return letter
            
    message = ''.join(map(encode_letter, message))
    return message
