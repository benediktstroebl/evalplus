
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
    swap_case_message = message.swapcase()
    swap_case_message = list(swap_case_message)
    for index, letter in enumerate(swap_case_message):
        if letter in vowels:
            swap_case_message[index] = chr(ord(letter) + 2)
    swap_case_message = ''.join(swap_case_message)
    return swap_case_message
            
    
