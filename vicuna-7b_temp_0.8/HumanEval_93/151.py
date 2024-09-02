
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
    # Sort the characters in the message
    message_sorted = sorted(message)
    
    # Reverse the string
    message_reversed = message_sorted[::-1]
    
    # Define an empty list to store the encoded characters
    encoded_chars = []
    
    # Iterate through the characters in the message
    for char in message_reversed:
        # If the char is a vowel
        if char in 'aeiouAEIOU':
            # Add a leading 0 to the encoded character
            encoded_chars.append('0' + str(ord(char) + 2))
        else:
            # Add the char as is to the encoded characters
            encoded_chars.append(char)
    
    # Return the encoded string
    return ''.join(encoded_chars)
