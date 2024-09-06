
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
    vowels = 'AEIOU'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            index_of_vowel = vowels.find(char)
            encoded_message += vowels[index_of_vowel + 2]
        else:
            encoded_message += char
    return encoded_message
