
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
    # <NAME>
    # Encode a message.
    # >>> encode("Hello World!")
    # 'hEllo wOrld!'
    # >>> encode("Howdy World!")
    # 'hOody wOrld!'
    new_message = []
    for i in message:
        if i in 'aeiouAEIOU':
            new_message.append(i.lower())
            new_message.append(i.lower())
        else:
            new_message.append(i)
    return ''.join(new_message)
