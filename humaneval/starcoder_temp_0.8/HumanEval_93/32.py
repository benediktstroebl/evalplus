
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
    encode_map = str.maketrans(string.ascii_lowercase, string.ascii_uppercase, string.ascii_letters)
    encoded_message = message.translate(encode_map)
    for vowel in string.ascii_letters:
        if vowel in encoded_message:
            vowel_position = encoded_message.find(vowel)
            encoded_message = encoded_message[:vowel_position + 2] + vowel_position + encoded_message[vowel_position + 1:]
    return encoded_message
