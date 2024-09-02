
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
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    if not isinstance(message, str):
        raise TypeError("Message must be a string.")
    
    encoded_message = ''
    
    for char in message:
        if char in vowels:
            position = vowels.index(char)
            if position < (len(vowels) - 1):
                encoded_message += vowels[(position + 2) % len(vowels)]
            else:
                encoded_message += vowels[0]
        else:
            encoded_message += char
            
    return encoded_message
