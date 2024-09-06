
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

    def encode_letter(l):
        if l.isalpha():
            if l.lower() in 'aeiou':
                return chr((ord(l) - ord('a') + 2) % 26 + ord('a'))
            else:
                return l.upper() if l.islower() else l.lower()
        else:
            return l

    return "".join(encode_letter(l) for l in message)
