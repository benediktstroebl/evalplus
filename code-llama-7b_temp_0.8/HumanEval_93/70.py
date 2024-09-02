
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
    # Pick out the vowels from message
    vowels = 'aeiou'
    encoded_message = ""
    for letter in message:
        if letter.lower() in vowels:
            letter_num = vowels.find(letter.lower())
            if letter.isupper():
                encoded_message += vowels[letter_num + 2].upper()
            else:
                encoded_message += vowels[letter_num + 2].lower()
        else:
            encoded_message += letter

    return encoded_message
    
