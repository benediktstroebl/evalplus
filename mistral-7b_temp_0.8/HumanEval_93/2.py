
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
    # Your code here
    vowels = 'aeiou'
    my_list = []
    my_list.append(message[0].lower())
    for i in range(1, len(message)):
        if message[i].lower() in vowels:
            my_list.append(message[i - 1].lower())
            my_list.append(vowels[vowels.index(message[i].lower()) + 2])
        else:
            my_list.append(message[i].lower())
    return ''.join(my_list)

