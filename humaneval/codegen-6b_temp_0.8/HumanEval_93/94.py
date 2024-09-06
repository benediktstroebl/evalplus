
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
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    result = ''

    for i in range(len(message)):
        char = message[i]
        if char.lower() not in alphabet:
            result += char
            continue
        index = alphabet.find(char.lower())
        index += 2
        
        #if index >= len(alphabet):
        #    index -= len(alphabet)
        
        result += alphabet[index]

    return result
