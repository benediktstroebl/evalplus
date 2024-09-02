
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
    '''
    replace vowels with the letter that appears 2 places ahead 
    of that vowel in the english alphabet.
    '''
    message = message.lower()
    # new_message = ''
    # for letter in message:
    #     if letter in ['a','e','i','o','u']:
    #         new_message += message.replace(letter,chr(ord(letter)+2))
    #     else:
    #         new_message += letter
    # return new_message
    '''
    Idea: 
    The main goal is to replace all vowels with the letter that 
    appears 2 places ahead of it in the alphabet. 
    In other words, we find the index of the vowel and add 2 to it, 
    which means the next vowel will appear 2 places later in the alphabet. 
    '''
    vowels = set('aeiou')
    new_message = []
    for letter in message:
        if letter in vowels:
            index = message.index(letter)
            new_message.append(message.replace(letter,chr(ord(letter)+2)))
        else:
            new_message.append(letter)
    return ''.join(new_message)
