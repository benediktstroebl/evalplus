
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
    msg = message
    a = 97
    e = 101
    i = 105
    o = 111
    u = 117
    v = 121
    w = 119
    y = 121
    x = 120
    vowels = (a,e,i,o,u,v,w,y,x)
    # a = 97
    # e = 101
    # i = 105
    # o = 111
    # u = 117
    # v = 121
    # w = 119
    # y = 121
    # x = 120
    new_msg = []
    for ch in msg:
        if ch in vowels:
            index = vowels.index(ch)
            if index == 0:
                index = 9
            elif index == 9:
                index = 0
            else:
                index -= 1
