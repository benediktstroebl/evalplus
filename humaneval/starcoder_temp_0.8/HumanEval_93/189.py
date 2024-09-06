
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

    # Initialize empty string
    encoded_message = ''
    
    # For every character in the message
    for c in message:

        # If the character is a letter
        if c.isalpha():

            # Shift the character by 2 places
            if c.isupper():
                c = ord(c) + 2
                encoded_message += chr(c)
            else:
                c = ord(c) + 2
                encoded_message += chr(c).lower()
        else:
            encoded_message += c

    return encoded_message
