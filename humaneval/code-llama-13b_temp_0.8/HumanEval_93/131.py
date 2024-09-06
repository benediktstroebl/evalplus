
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
    vowels = "aeiou"
    vowel2char = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 's',
        'u': 'v',
    }
    result = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()
            if char in vowels:
                char = vowel2char[char]
        result += char
    return result
    
