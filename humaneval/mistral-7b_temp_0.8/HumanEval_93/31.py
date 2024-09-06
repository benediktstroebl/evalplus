
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
    for letter in message:
        message_list.append(letter)
    message_list.sort()
    index = message_list.index('a')
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_index = []
    for letter in vowels:
        vowels_index.append(message_list.index(letter))
    for i in range(len(message)):
        if message[i].lower() in vowels:
            message = message.replace(message[i].lower(),message_list[vowels_index[vowels.index(message[i].lower())]+2])
        else:
            if message[i].isupper():
                message = message.replace(message[i],message[i].lower())
            else:
                message = message.replace(message[i],message[i].upper())
    return message

