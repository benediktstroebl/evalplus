
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

    swapcase_str = message.swapcase()
    swapcase_list = list(swapcase_str)
    vowels = 'aeiou'
    for i in range(len(swapcase_list)):
        if swapcase_list[i] in vowels:
            swapcase_list[i] = swapcase_list[(vowels.index(swapcase_list[i])+2)%len(vowels)]

    return ''.join(swapcase_list)

