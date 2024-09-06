
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
    vowels = ('a','e','i','o','u')
    new_str = ''
    
    # Swap case
    for c in message:
        if c.isalpha():
            new_str += c.upper() if c.islower() else c.lower()
        else:
            new_str += c
            
    # replace vowels
    for i, c in enumerate(new_str):
        if c in vowels:
            index = (vowels.index(c) + 2) % 5
            new_str = new_str[:i] + vowels[index] + new_str[i+1:]
            
    return new_str
            
            
