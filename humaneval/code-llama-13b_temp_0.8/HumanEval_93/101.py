
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
    encoded_message = ''
    vowels = 'aeiouAEIOU'
    for letter in message:
        if letter in vowels:
            if letter.isupper():
                encoded_letter = chr(ord(letter) + 2 % 26)
            elif letter.islower():
                encoded_letter = chr(ord(letter) + 2)
        else:
            encoded_letter = letter
        encoded_message += encoded_letter
    return encoded_message
