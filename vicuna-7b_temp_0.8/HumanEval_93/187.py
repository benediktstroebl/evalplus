
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
    message = message.upper()
    encoded_message = ''
    for letter in message:
        if letter in 'aeiouAEIOU':
            if letter == 'a':
                encoded_letter = 'B'
            elif letter == 'e':
                encoded_letter = 'D'
            elif letter == 'i':
                encoded_letter = 'F'
            elif letter == 'o':
                encoded_letter = 'H'
            else:
                encoded_letter = letter
        else:
            encoded_letter = letter
        encoded_message += encoded_letter
    return encoded_message
