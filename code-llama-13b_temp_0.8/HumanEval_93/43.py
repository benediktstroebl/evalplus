
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
    vowels = 'aeiou'
    encoded_message = ''
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                encoded_letter = chr(ord(letter) + 2 % 26)
                if letter.isupper():
                    encoded_letter = encoded_letter.upper()
            else:
                encoded_letter = letter.swapcase()
        else:
            encoded_letter = letter
        encoded_message += encoded_letter
    return encoded_message




