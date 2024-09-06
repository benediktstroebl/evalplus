
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
    
    # encode message
    encoded_message = ''
    for character in message:
        
        # test for lower case
        if character.islower():
            encoded_message += character.upper()
        
        # test for upper case
        elif character.isupper():
            encoded_message += character.lower()
        
        # test for vowels and replace with the alphabet
        else:
            new_character = character
            if character == 'a':
                new_character = 'S'
            elif character == 'e':
                new_character = 'F'
            elif character == 'i':
                new_character = 'K'
            elif character == 'o':
                new_character = 'B'
            elif character == 'u':
                new_character = 'J'
                
            encoded_message += new_character
                
    return encoded_message

