
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
    
    # create an empty string
    new_message = ""
    for letter in message:
        if letter.isalpha():
            # check if letter is a vowel
            if letter.upper() in "AEIOU":
                new_message += letter.swapcase()
            else:
                # letter is not a vowel
                new_message += letter
        else:
            new_message += letter
        
    return new_message
    
