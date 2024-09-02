
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

    
    new_message = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in message:
        if char.isalpha() == True:
            new_message = new_message + char.swapcase()
        else:
            new_message = new_message + char
            
    for vowel in vowels:
        vowel_count = new_message.count(vowel)
        if vowel_count > 0:
            for i in range(vowel_count):
                new_index = new_message.find(vowel)
                new_message = new_message[:new_index] + vowels[vowel_count + 1] + new_message[new_index + 1:]
                
    return new_message
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
