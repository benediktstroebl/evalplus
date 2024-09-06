
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
    message_list = list(message)

    for i in range(len(message_list)):
        if message_list[i].islower():
            message_list[i] = message_list[i].upper()
        elif message_list[i].isupper():
            message_list[i] = message_list[i].lower()

    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(message_list)):
        if message_list[i] in vowels:
            message_list[i] = message_list[i+2]

        if message_list[i].islower() and message_list[i] not in vowels:
            message_list[i] = message_list[i].upper()
        elif message_list[i].isupper() and message_list[i] not in vowels:
            message_list[i] = message_list[i].lower()

    return ''.join(message_list)

