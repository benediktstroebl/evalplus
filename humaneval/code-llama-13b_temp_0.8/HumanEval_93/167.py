
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
    
    vowels = "aeiouAEIOU"
    char_map = {
        vowel: chr(ord(vowel) + 2)
        for vowel in vowels
    }
    return "".join(
        char_map.get(char, char.lower())
        if char.isalpha() else char
        for char in message
    )
