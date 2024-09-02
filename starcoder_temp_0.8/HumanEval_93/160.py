
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
    
    output = ''
    #Loop through message
    for char in message:
        #if char is vowel, add second letter of alphabet
        if char.lower() in 'aeiou':
            output += chr(ord(char.lower()) + 2)
        else:
            #if not, add char
            output += char
    return output
