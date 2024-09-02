
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

    pass
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    encoded = ''
    
    for char in message:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
            else:
                char = char.upper()
        
        if char in vowels:
            nextVowel = vowels[vowels.index(char) + 2]
            encoded += nextVowel
        else:
            encoded += char
    
    return encoded
