
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
    message_list = []
    message = message.upper()
    for letter in message:
        if letter in string.ascii_letters:
            if letter in vowels:
                index = vowels.index(letter)
                message_list.append(vowels[index + 2])
            else:
                index = consonants.index(letter)
                message_list.append(consonants[index + 2])
        else:
            message_list.append(letter)
    return ''.join(message_list)
