
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
    
    encoded_message = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in message:
        # swapping the case
        if char.isalpha():
            if char.islower():
                char = char.upper()
            elif char.isupper():
                char = char.lower()
                
        # replace vowels
        if char.lower() in vowels:
            char = vowels[(vowels.index(char.lower()) + 2) % len(vowels)]
        
        encoded_message += char
    
    return encoded_message
