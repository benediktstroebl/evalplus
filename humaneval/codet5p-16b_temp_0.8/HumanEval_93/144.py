
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

    new_message = message.lower()
    vowels = 'aeiou'
    new_message = [char for char in new_message]
    vowel_replace = [char for char in new_message if char in vowels]
    i = 0
    for char in new_message:
        if char in vowels:
            i += 2
            new_message[new_message.index(char)] = vowel_replace[i]
            i -= 2
        else:
            i += 1
            new_message[new_message.index(char)] = vowel_replace[i]
    return ''.join(new_message)
