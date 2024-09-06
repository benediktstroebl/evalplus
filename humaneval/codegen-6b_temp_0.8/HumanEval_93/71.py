
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
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    def group(word):
        
        s = ''
        
        for i in xrange(len(word)):
            
            if word[i].lower() in vowels:
                s += word[i].upper()
            else:
                s += word[i]
                
        return s
    
    return group(message.lower())
    
    








