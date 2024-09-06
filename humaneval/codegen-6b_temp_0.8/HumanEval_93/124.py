
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
    vowels = set('AEIOUaeiou') 
    message = message.upper()
    rep = {'A':'4','E':'3','G':'6','I':'1','O':'0','U':'5'} 
    new = [rep[i] if i in vowels else i for i in message] 
    return ''.join(new)
    
    
import doctest
doctest.testmod()
