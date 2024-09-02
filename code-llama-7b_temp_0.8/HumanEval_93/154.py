
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
    newMessage = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vowels = 'aeiouAEIOU'
    vowelMap = dict(zip(vowels,alpha[2:]+alpha[0:2]))
    
    for ch in message:
        if ch in alpha:
            if ch in vowels:
                newMessage += vowelMap[ch]
            else:
                newMessage += alpha[(alpha.index(ch)+2)%26]
        elif ch in alpha2:
            newMessage += alpha2[(alpha2.index(ch)+2)%26]
        else:
            newMessage += ch
    return newMessage


