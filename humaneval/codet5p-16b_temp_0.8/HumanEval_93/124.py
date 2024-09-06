
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

    new_message = message
    message_list = list(message)
    vowels = ['a', 'e', 'i', 'o', 'u']
    for index in range(len(message_list)):
        if message_list[index].isupper():
            message_list[index] = message_list[index].lower()
    for index in range(len(message_list)):
        if message_list[index] in vowels:
            if message_list[index].islower():
                message_list[index] = message_list[index].upper()
    
    for index in range(len(message_list)):
        if message_list[index] in vowels:
            vowel_position = vowels.index(message_list[index]) + 2
            message_list[index] = vowels[vowel_position]
    
    new_message = ''.join(message_list)
    return new_message
    
    
