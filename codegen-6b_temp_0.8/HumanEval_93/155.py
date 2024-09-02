
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
    # https://www.w3schools.com/python/python_strings_convert.asp
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    final = ""
    for letter in message:
        if letter in vowels:
            final += chr(ord('a') + 2)
        else:
            final += letter
    
    return final
