
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

    assert message.isalpha()
    
    new_message = message.swapcase()
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_message = new_message.replace(vowels[0], chr( ord(vowels[0]) + 2))
    new_message = new_message.replace(vowels[1], chr( ord(vowels[1]) + 2))
    new_message = new_message.replace(vowels[2], chr( ord(vowels[2]) + 2))
    new_message = new_message.replace(vowels[3], chr( ord(vowels[3]) + 2))
    new_message = new_message.replace(vowels[4], chr( ord(vowels[4]) + 2))

    return new_message

