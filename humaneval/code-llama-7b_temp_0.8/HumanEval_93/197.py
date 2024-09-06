
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
    vowels = 'AEIOUaeiou'
    vowel_idx = 0
    encoded_message = []
    for char in message:
        if char in vowels:
            vowel_idx = vowels.index(char)
            if vowel_idx+2 > 4:
                encoded_message.append(vowels[(vowel_idx+2)-5])
            else:
                encoded_message.append(vowels[vowel_idx+2])
        else:
            if char.isupper():
                encoded_message.append(char.swapcase())
            else:
                encoded_message.append(char)
    return ''.join(encoded_message)
