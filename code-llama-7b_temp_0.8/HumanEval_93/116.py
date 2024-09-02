
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
    import string
    def is_vowel(c):
        return c in "aeiou"

    vowels_pos = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}

    def encode_char(c):
        if c in string.ascii_lowercase:
            if c in vowels_pos:
                return string.ascii_lowercase[vowels_pos[c] + 2]
            else:
                return c.swapcase()
        else:
            return c

    return "".join(map(encode_char, message))

