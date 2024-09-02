
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
    # Invert the case of the letters
    inverted_message = [letter.lower() if letter.isupper() else letter.upper() for letter in message]
    # Replace the vowels with the letter that appears 2 places ahead of the vowel
    for index, letter in enumerate(inverted_message):
        if letter in VOWELS:
            inverted_message[index] = VOWELS[(VOWELS.index(letter)+2)%len(VOWELS)]
    return ''.join(inverted_message)
