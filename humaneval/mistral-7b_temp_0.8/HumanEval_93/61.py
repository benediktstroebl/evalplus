
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
    encode_dict = {char: char.upper() if char.islower() else char.lower() for char in message}
    swap_dict = {vowel: vowel.upper() if vowel.islower() else vowel.lower() for vowel in vowels}
    encode_dict.update(swap_dict)
    return ''.join(encode_dict[char] for char in message)
