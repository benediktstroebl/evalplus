
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
    encode_message = ''
    for char in message:
        if char.lower() in vowels:
            # print ord(char), ord('z') - ord(char) + 1
            encode_message += chr(ord('z') - ord(char) + 1)
        else:
            encode_message += char
    return encode_message

