
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
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    message = message.upper()
    answer = ""
    for i in message:
        if i =='':
            answer = answer + " "
        else:
            index = alphabet.index(i)
            answer = answer + alphabet[(index+2)%26]

    return answer
