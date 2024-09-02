
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
    new_msg = ''
    for i in message:
        if i.isalpha():
            if i.isupper():
                new_msg += i.lower()
            else:
                new_msg += i.upper()
        else:
            new_msg += i
    vowels = 'aeiou'
    new_msg = new_msg.replace(' ','')
    for i in range(len(new_msg)):
        if new_msg[i] in vowels:
            new_msg = new_msg[:i] + vowels[(vowels.index(new_msg[i])+2)%5] + new_msg[i+1:]
    return new_msg

