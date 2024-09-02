
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
    enc = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                enc += char.lower()
            elif char.islower():
                if char == 'a':
                    enc += chr(98)
                elif char == 'e':
                    enc += chr(101)
                elif char == 'i':
                    enc += chr(105)
                elif char == 'o':
                    enc += chr(111)
                elif char == 'u':
                    enc += chr(117)
                else:
                    enc += chr(ord(char) + 2)
        else:
            enc += char
    return enc
