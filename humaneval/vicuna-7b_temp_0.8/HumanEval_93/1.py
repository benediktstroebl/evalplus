
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
    # initialize a string to store the encoded message
    encoded_message = ''
    
    # loop through each character in the message
    for char in message:
        # swap case
        if char.isupper():
            encoded_char = char.lower()
        else:
            encoded_char = char
        
        # replace vowels with their corresponding vowel 2 places ahead
        if char.isalpha() and char in 'aeiouAEIOU':
            # get index of current vowel in english alphabet
            index = 'aeiou'.index(char)
            
            # get vowel 2 places ahead in english alphabet
            next_index = index + 2
            
            # replace current vowel with its equivalent in english alphabet
            if index == 'a':
                encoded_char = chr(next_index + 97)  # 'A'
            elif index == 'e':
                encoded_char = chr(next_index + 122)  # 'E'
            elif index == 'i':
                encoded_char = chr(next_index + 91)  # 'I'
            elif index == 'o':
                encoded_char = chr(next_index + 154)  # 'O'
            elif index == 'u':
                encoded_char = chr(next_index + 185)  # 'U'
        else:
            # do nothing
            pass
        
        # add encoded character to the encoded message
        encoded_message += encoded_char
    
    return encoded_message
