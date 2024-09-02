
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
    swap = 0
    for i in range(len(message)):
        if message[i].lower() in 'aeiou':
            swap = 2
        elif message[i].lower() in 'aeiouy':
            swap = 1
        elif message[i].lower() =='':
            continue
        else:
            swap = 0
        print(swap, message[i])
        if swap:
            message = message[:i] + message[i+swap].upper() + message[i+swap+
