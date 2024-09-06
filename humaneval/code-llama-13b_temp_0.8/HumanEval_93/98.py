
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
    alpha = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    # Solution 1
    vowels = ['a','e','i','o','u']
    message = message.lower()
    message = list(message)
    for i in range(len(message)):
        if message[i] in vowels:
            message[i] = alpha[(alpha.index(message[i])+2)%26]
    return "".join(message)
    
    # Solution 2
    vowels = 'aeiou'
    message = message.lower()
    for i in vowels:
        message = message.replace(i, vowels[(vowels.index(i)+2)%5])
    return message

    
    # Solution 3
    vowels = 'aeiou'
    message = message.lower()
    for i in vowels:
        message = message.replace(i, vowels[(vowels.index(i)+2)%5])
    message = message.swapcase()
    return message
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
