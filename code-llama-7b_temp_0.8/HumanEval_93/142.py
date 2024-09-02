
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
    # Trivial method
    # return message.swapcase()
    
    # Letter to vowel replace
    vowels = 'aeiouAEIOU'
    vowel_dict = {'a':'f','e':'g','i':'h','o':'j','u':'k'}
    output_str = ''
    for char in message:
        if char in vowels:
            output_str += vowel_dict[char]
        else:
            output_str += char
    # Change case
    output_str = output_str.swapcase()
    return output_str
    
