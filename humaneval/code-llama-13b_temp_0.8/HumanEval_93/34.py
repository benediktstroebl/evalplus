
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
    encoded = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                encoded += chr((ord(letter) - ord('A') + 2) % 26 + ord('A'))
            else:
                encoded += chr((ord(letter) - ord('a') + 2) % 26 + ord('a'))
        else:
            encoded += letter
    return encoded
    
    
