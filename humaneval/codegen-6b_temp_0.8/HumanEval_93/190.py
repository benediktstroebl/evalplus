
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
    # Replace the vowels
    message = message.lower().replace('a', '4')
    message = message.replace('e', '3')
    message = message.replace('o', '0')
    message = message.replace('u', '1')

    # Swap the letters
    new_message = ''
    for index in range(len(message)):
        # Check if it is a letter
        if ord(message[index]) >= 97 and ord(message[index]) <= 122:
            new_message += chr(ord(message[index]) + 2)
        else:
            new_message += message[index]
    return new_message

