
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

    # create a copy of the message, so that the original message is 
    # not modified
    message_copy = message
    
    # set an empty string for the encoded message
    encoded_message = ''
    
    # check if the message is empty, and if so, return an empty string
    if message_copy == '':
        return ''
    else:
        # change all the characters to upper case
        message_copy = message_copy.upper()
        
        # loop through each character in the message
        for character in message_copy:
            
            # check if the character is a vowel
            if character == 'A' or character == 'E' or character == 'I' \
            or character == 'O' or character == 'U':
                # find the index of the vowel
                vowel_index = message_copy.index(character)
                
                # calculate the position in the alphabet of the letter 
                # that appears 2 places ahead of the vowel
                new_letter_position = ((vowel_index + 2) % 26) + 1
                
                # create the new letter
                new_letter = chr(ord('A') + new_letter_position - 1)
                
                # add the new letter to the encoded message
                encoded_message += new_letter
                
            else:
                # otherwise, just add the character to the encoded message
                encoded_message += character
                
        return encoded_message
        
