
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
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                message[i] = message[i].lower()
            elif message[i].islower():
                message[i] = message[i].upper()
            
            if message[i] == 'a':
                message[i] = 'E'
            elif message[i] == 'e':
                message[i] = 'I'
            elif message[i] == 'i':
                message[i] = 'O'
            elif message[i] == 'o':
                message[i] = 'U'
            elif message[i] == 'u':
                message[i] = 'A'
                
    return "".join(message)
