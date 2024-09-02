
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
    
    # each vowel is replaced with the letter that appears 2 places 
    # ahead of it in the english alphabet
    vowels = [letter for letter in string.ascii_lowercase if letter in 'aeiou']
    message = message.lower()
    l = list(message)
    for i, letter in enumerate(l):
        if letter in vowels:
            l[i] = vowels[(vowels.index(letter)+2)%len(vowels)]
    return "".join(l)
    
