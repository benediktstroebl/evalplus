
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
    new_message = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_dict = {vowel: chr(ord(vowel) + 2) for vowel in vowels}
    for letter in message:
        if letter.lower() in vowels:
            new_message.append(vowel_dict[letter.lower()])
        else:
            new_message.append(letter.swapcase())
    return ''.join(new_message)
