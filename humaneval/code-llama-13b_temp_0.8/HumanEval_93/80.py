
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
    vowels = 'aeiouAEIOU'
    message_encode = ''
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                letter_index = vowels.index(letter.lower())
                letter = vowels[letter_index + 2] if letter_index < 4 else vowels[letter_index - 2]
            letter = letter.swapcase()
        message_encode += letter
    return message_encode

