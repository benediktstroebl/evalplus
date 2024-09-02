
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
    message = message.upper()
    encoded = ""
    for char in message:
        if char.isspace():
            encoded += char
        elif char.isalpha():
            # swap case
            if char.islower():
                encoded += char.upper()
            else:
                encoded += char.lower()
        else:
            encoded += char
    # replace vowels
    vowels = "aeiouAEIOU"
    next_vowel_index = {}
    for char in vowels:
        next_vowel_index[char] = vowels.index(char) + 2
    for char in encoded:
        if char in next_vowel_index:
            encoded += next_vowel_index[char]
    return encoded
