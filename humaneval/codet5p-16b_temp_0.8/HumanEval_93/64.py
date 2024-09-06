
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

    
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    new_message = ''
    
    for char in message:
        if char.isalpha():
            if char.islower():
                new_message += char.upper()
            else:
                new_message += char.lower()
        else:
            new_message += char
        
    for char in new_message:
        if char in vowels:
            new_message = new_message.replace(char, chr(ord(char)+2))
    
    return new_message
        
