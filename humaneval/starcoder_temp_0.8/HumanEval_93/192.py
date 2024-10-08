
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
    
    message = message.lower()
    encoded_message = ''
    
    for letter in message:
        if letter in vowels:
            vowel_index = vowels.index(letter)
            new_letter = vowels[vowel_index + 2]
        else:
            new_letter = letter
            
        encoded_message += new_letter
        
    return encoded_message
