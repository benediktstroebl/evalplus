
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
    if message == '':
        return message
    
    # Taking the message and adding a space at the end to make sure that the last letter in the message is added to the answer
    message += ' '
    
    # Making the new message string to be returned at the end
    new_message = ''
    
    # Going through the message
    for letter in message:
        # If the letter is a vowel
        if letter in 'aeiouAEIOU':
            # Add the letter 2 places ahead of the vowel in the english alphabet to the new message
            new_message += chr((ord(letter) + 2) % 26 + 65)
        # If the letter is not a vowel
        else:
            # Add the letter to the new message
            new_message += chr((ord(letter) - 32) % 26 + 65)
            
    # Returning the new message
    return new_message
    
