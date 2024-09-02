
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
    # create a variable to store the result
    encoded = ''
    # loop through the message
    for char in message:
        # check if it is a vowel
        if char in 'aeiou':
            # encode the vowel
            encoded = encoded + 'abcdefghijklmnopqrstuvwxyz'[ord(char) - ord('a') + 2]
        else:
            # otherwise encode the character
            if char.isupper():
                encoded = encoded + char.lower()
            else:
                encoded = encoded + char.upper()
    # return the result
    return encoded
