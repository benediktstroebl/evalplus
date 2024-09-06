
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
    # Create a copy of the input message
    encoded_message = message
    
    # Create a dictionary to store the encoding
    letters = 'abcdefghijklmnopqrstuvwxyz'
    encoding = {}
    
    # Populate the encoding dictionary
    for i in range(len(letters)):
        encoding[letters[i]] = letters[((i + 2) % 26)]
    
    # Create a list of vowels
    vowels = 'aeiou'
    
    # Iterate through the message
    for i in range(len(encoded_message)):
        # Check for vowels and encode them
        if encoded_message[i] in vowels:
            encoded_message = encoded_message[:i] + encoding[encoded_message[i]] + encoded_message[i + 1:]
        
        # Check for uppercase letters and encode them
        if encoded_message[i].isupper():
            encoded_message = encoded_message[:i] + encoded_message[i].lower()
        # Check for lowercase letters and encode them
        if encoded_message[i].islower():
            encoded_message = encoded_message[:i] + encoded_message[i].upper()

    # Return the encoded message
    return encoded_message
    
