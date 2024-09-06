
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
    vowels = 'AEIOU'
    # The new message
    new = ''
    for char in message:
        # Check if the char is in the vowels
        if char in vowels:
            # If the char is a vowel, we find the char that is 2 places ahead of it in the alphabet
            new += chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
        else:
            # Otherwise we just append the same character.
            new += char
    return new.swapcase()
