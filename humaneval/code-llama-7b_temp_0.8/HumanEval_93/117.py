
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
    
    # temporary string to hold encoded message
    encoded_message = ''
    
    # temporary string to hold vowels in message
    vowels = ''
    
    # temporary integer to hold value of each vowel in message
    vowel_values = [65, 97, 73, 69, 79, 78, 83]
    
    # check each letter in message
    for letter in message:
        
        # if letter is a vowel
        if ord(letter) in vowel_values:
            
            # store vowel in temporary string
            vowels += letter
            
            # store vowel in encoded_message
            if ord(letter) < 97:
                encoded_message += chr(ord(letter) + 2)
            
            # store vowel in encoded_message
            elif ord(letter) > 90:
                encoded_message += chr(ord(letter) - 2)
        
        # if letter is not a vowel
        else:
            
            # store letter in encoded_message
            if ord(letter) > 90:
                encoded_message += chr(ord(letter) - 32)
            
            # store letter in encoded_message
            else:
                encoded_message += chr(ord(letter) + 32)
    
    # loop through vowels
    for i in range(len(vowels)):
        
        # if letter is not in the correct position
        if ord(vowels[i]) > ord(vowels[i-1]) + 2:
            
            # store letter in encoded_message
            encoded_message = encoded_message[:i] + chr(ord(vowels[i]) - 2) + encoded_message[i:]
            
            # move to next letter
            i += 1
    
    # return encoded_message
    return encoded_message

