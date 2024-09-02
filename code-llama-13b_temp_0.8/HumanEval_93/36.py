
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
    encoded_message = ""
    vowels = "aeiou"
    vowels_dict = {'a': 'c', 'e': 'g', 'i': 'i', 'o': 'k', 'u': 'm'}
    for char in message:
        if char.islower():
            char = char.upper()
        if char in vowels:
            char = vowels_dict[char]
        encoded_message += char
    return encoded_message
