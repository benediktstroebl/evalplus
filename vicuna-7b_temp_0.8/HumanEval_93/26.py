
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
    # Initialize an empty string to hold the encoded message
    encoded_message = ""
    
    # Iterate through the characters in the message
    for c in message:
        # If the character is a vowel, replace it with its vowel 
        # followed by the next letter in the english alphabet
        if c.lower() in "aeiou":
            encoded_message += c + chr(ord(c) + 2)
        else:
            # Otherwise, just append the character to the 
            # encoded message
            encoded_message += c
    
    return encoded_message
