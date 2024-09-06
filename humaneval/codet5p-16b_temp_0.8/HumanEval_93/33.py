
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

    new_message = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in message:
        if i.isalpha():
            new_message.append(i.swapcase())
        else:
            new_message.append(i)
    for j in range(len(new_message)):
        if new_message[j] in vowels:
            new_message[j] = new_message[j + 2]
    return ''.join(new_message)
