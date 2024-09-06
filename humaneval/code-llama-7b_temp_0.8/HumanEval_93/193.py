
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

    # Create list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # Create empty string to store encoded message
    encoded_message = ""

    # Loop through message
    for letter in message:
        if letter in vowels:
            # Append next vowel to encoded message
            encoded_message += vowels[(vowels.index(letter) + 2) % len(vowels)]
        else:
            # Append decoded letter to encoded message
            if letter.islower():
                encoded_message += letter.upper()
            else:
                encoded_message += letter.lower()
    
    # Return encoded message
    return encoded_message
