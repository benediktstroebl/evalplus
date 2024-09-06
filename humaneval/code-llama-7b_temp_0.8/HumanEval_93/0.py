
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

    # Elements of the python alphabet.
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Transform all letters in lower case.
    message = message.lower()

    # Create the new message.
    new_message = ""

    # Iterate through all characters of the message.
    for character in message:
        # Add to the new message.
        if character in alpha:
            # If it is a vowel, insert a vowel.
            if character in "aeiou":
                # Find the position of the character.
                pos = alpha.find(character)

                # Add the character 2 positions ahead.
                new_message += alpha[pos + 2]
            # Add the character itself.
            else:
                # Find the position of the character.
                pos = alpha.find(character)

                # Add the character 1 position ahead.
                new_message += alpha[pos + 1]
        else:
            # Add the character itself.
            new_message += character

    # Return the new message.
    return new_message
