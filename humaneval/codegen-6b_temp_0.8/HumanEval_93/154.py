
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
    encoded_message = message.swapcase()
    vowels = 'aeiouAEIOU'
    def helper(letter):
        return vowels[(vowels.find(letter) + 2) % 5]
    return encoded_message.translate(str.maketrans(vowels, ''.join(map(helper, encoded_message))))
