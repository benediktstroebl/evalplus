
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
    vowels = ('a','e','i','o','u')
    translation_table = message.maketrans('aeiou', 'AEIOU', ' \t\n\r\v')
    message_upper = message.upper().translate(translation_table)
    
    encoded_message = ""
    for letter in message_upper:
        if letter in vowels:
            index = vowels.index(letter)
            encoded_message += vowels[(index + 2) % 5]
        else:
            encoded_message += letter
    
    return encoded_message
