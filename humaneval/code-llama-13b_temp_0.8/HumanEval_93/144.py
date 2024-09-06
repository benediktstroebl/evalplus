
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
    if not isinstance(message, str):
        raise TypeError("message must be a string")
    
    encoded_message = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                encoded_message += letter.upper()
            elif letter.isupper():
                encoded_message += letter.lower()
        elif letter in vowels:
            for vowel in vowels:
                if letter == vowel:
                    encoded_message += vowels[vowels.index(vowel)+2]
        else:
            encoded_message += letter
    return encoded_message
            
    
    
    
