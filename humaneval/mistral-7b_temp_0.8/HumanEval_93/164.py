
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
    message=message.lower()
    result=list()
    for i in message:
        if i.isalpha():
            if i in 'aeiou':
                result.append(chr((ord(i)+2)%26+ord('a')))
            else:
                result.append(chr((ord(i)-32)%26+ord('a')+32))
        else:
            result.append(i)
    return ''.join(result)

