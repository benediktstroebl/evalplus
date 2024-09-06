
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
    # replace case
    message = message.lower()
    for i in range(len(message)):
        if message[i].isupper():
            message = message[:i] + message[i].lower() + message[i+1:]
    # replace vowels
    replace = 'aeiou'
    for i in range(len(message)):
        if message[i] in replace:
            replace_index = replace.index(message[i])
            replace_index = replace_index + 2
            if replace_index >= 26:
                replace_index -= 26
            message = message[:i] + chr(ord(replace[replace_index])+ord('a')) + message[i+1:]
    return message

