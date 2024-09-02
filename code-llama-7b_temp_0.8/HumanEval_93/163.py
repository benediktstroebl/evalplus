
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
    # YOUR CODE HERE
    encoded_message = []
    for i in message:
        if i.isupper():
            encoded_message.append(i.lower())
        elif i.islower():
            encoded_message.append(i.upper())
        elif i in 'aeiou':
            index = ord(i) + 2
            if index > 122:
                index = index - 26
            encoded_message.append(chr(index))
        else:
            encoded_message.append(i)
    return ''.join(encoded_message)
