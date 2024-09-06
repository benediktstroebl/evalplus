
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
    # Your code here
    # Get a list of the characters in the message
    message = list(message)
    # Create an empty string to hold the encoded message
    encoded_message = ""
    # Go through each character in the message
    for char in message:
        # If the character is a vowel
        if char in "aeiou":
            # Add the character that appears 2 places ahead of the vowel
            # in the alphabet
            encoded_message += chr(ord(char) + 2)
        # Otherwise, if the character is not a vowel, just add it to the 
        # encoded message
        else:
            encoded_message += char
    # Return the encoded message
    return encoded_message
