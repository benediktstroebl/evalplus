
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
    # s1 = message.swapcase()
    # vowels = set('aeiou')
    # for v in vowels:
    #     s1 = s1.replace(v, chr((ord(v) - ord('a') + 2) % 26 + ord('a')))
    # return s1
    vowels = set('aeiou')
    encode = lambda m: chr((ord(m) - ord('a') + 2) % 26 + ord('a')) if m in vowels else m
    return message.swapcase().translate(encode)
    
    
    


