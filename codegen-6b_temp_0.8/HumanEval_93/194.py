
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
    # map(lambda c: {'a':'@', 'e':'3', 'o':'0', 'u':'~', 'i':'1', 'A':'4',
    #                  'E':'3',
    #                  'O':'0', 'U':'~', 'I':'1'}[c] if c in 'aeoiuAEOIU' else c
    #            ,message.lower())
    
    res = ''
    for c in message.lower():
        if c in 'aeoiu':
            res += c + chr(ord(c) + 2)
        else:
            res += c
    return res

