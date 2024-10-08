
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
    message = message.upper() # convert message to uppercase
    encoded_message = ''
    for letter in message:
        if letter.isalpha(): # check if letter is a vowel
            index = letter.isalpha()-1 # subtract 1 from index because vowels appear before their index in alphabet
            encoded_letter = chr(ord('a') + index) # add index to letter to get encoded letter
        else:
            encoded_letter = letter
        encoded_message += encoded_letter
    return encoded_message
