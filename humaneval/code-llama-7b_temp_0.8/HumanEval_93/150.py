
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
    message_dict = {}
    message_list = list(message)
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i] in ['a','e','i','o','u']:
                message_dict[i] = chr((ord(message[i])+2)%26+ord('A'))
            else:
                message_dict[i] = chr((ord(message[i])+1)%26+ord('A'))
        else:
            message_dict[i] = message[i]

    message_list = [message_dict[i] for i in range(len(message_list))]
    encoded_message = ''.join(message_list)
    return encoded_message
