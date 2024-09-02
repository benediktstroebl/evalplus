
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
    output = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(message)):
        if message[i] in vowels:
            vowel_index = message.index(message[i])
            output += message[vowel_index]
            output += message[vowel_index+2]
        else:
            output += message[i]
    return output
