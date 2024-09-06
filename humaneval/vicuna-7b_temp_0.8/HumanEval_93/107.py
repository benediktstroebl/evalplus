
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
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message_alphabet = alphabet[ord('A')-1:ord('Z')+1]
    encoded_message = ''
    for letter in message:
        if letter.lower() in message_alphabet:
            encoded_letter = message_alphabet[ord(letter)-ord('A')+2]
        else:
            encoded_letter = encoded_letter
        encoded_message += encoded_letter
    return encoded_message
