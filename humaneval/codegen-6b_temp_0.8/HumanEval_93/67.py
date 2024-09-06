
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
    
    # start with an empty string
    encoded_message = ''
    
    # loop through the message 
    for i in range(len(message)):
        # grab the i'th letter from the message
        letter = message[i]
        vowel = is_vowel(letter)
        
        # if it is a vowel
        if vowel:
            # grab the i+1 and i+2 letters from the message
            prev_letter = message[i-1] if i > 0 else ''
            next_letter = message[i+1] if i < len(message)-1 else ''
            next_next_letter = message[i+2] if i < len(message)-2 else ''
            
            # replace the vowels with the two letters 
            encoded_message += prev_letter + next_letter + next_next_letter
        
        # if not a vowel
        else:
            # add the letter to the encoded message
            encoded_message += letter
        
    # return the encoded message
    return encoded_message
