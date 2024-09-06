
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
    message_encoded = ''
    for i in message:
        if i == ' ':
            message_encoded += i
        else:
            vowels = 'aeiou'
            if i in vowels:
                message_encoded += vowels[(vowels.index(i)+2)%5]
            else:
                if i.isupper():
                    message_encoded += i.lower()
                else:
                    message_encoded += i.upper()
    return message_encoded
