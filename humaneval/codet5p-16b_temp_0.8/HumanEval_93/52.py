
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

    
    new = message.swapcase()
    vowels = 'aeiouAEIOU'
    new = new.replace('A', 'a')
    new = new.replace('E', 'e')
    new = new.replace('I', 'i')
    new = new.replace('O', 'o')
    new = new.replace('U', 'u')
    
    new = new.replace('a', 'A')
    new = new.replace('e', 'E')
    new = new.replace('i', 'I')
    new = new.replace('o', 'O')
    new = new.replace('u', 'U')
    
    for i in range(len(vowels)):
        new = new.replace(vowels[i], vowels[i+2])
    
    return new
