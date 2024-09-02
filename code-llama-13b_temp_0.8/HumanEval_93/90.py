
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_message = []
    
    for letter in message:
        if letter.isupper():
            new_message.append(letter.lower())
        elif letter.islower():
            new_message.append(letter.upper())
        elif letter in vowels:
            vowel_index = vowels.index(letter)
            new_message.append(vowels[vowel_index + 2])
        else:
            new_message.append(letter)
    
    return ''.join(new_message)
        
        
