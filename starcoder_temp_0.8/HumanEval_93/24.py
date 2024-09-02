
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
    
    message = list(message)
    # for letter in message:
    #     if letter in vowels:
    #         vowel_index = vowels.index(letter)
    #         new_letter = vowels[(vowel_index + 2) % len(vowels)]
    #         message[message.index(letter)] = new_letter
    #     elif letter in uppercase:
    #         message[message.index(letter)] = lowercase[uppercase.index(letter)]
    
    # message = ''.join(message)
    for i in range(len(message)):
        if message[i] in vowels:
            message[i] = vowels[(vowels.index(message[i]) + 2) % len(vowels)]
        elif message[i] in uppercase:
            message[i] = lowercase[uppercase.index(message[i])]
    
    return ''.join(message)
