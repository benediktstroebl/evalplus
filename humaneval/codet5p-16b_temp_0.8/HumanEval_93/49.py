
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

    
    def swap_case(message):
        """
        Write a function that takes a message, and encodes in such a 
        way that it swaps case of all letters, replaces all vowels in 
        the message with the letter that appears 2 places ahead of that 
        vowel in the english alphabet. 
        Assume only letters. 
        
        Examples:
        >>> swap_case('test')
        'tgst'
        >>> swap_case('This is a message')
        'thKS KS c MGSSCGG'
        """
        
        vowels = 'AEIOU'
        new_msg = []
        
        for letter in message:
            if letter in vowels:
                new_msg.append(vowels[vowels.index(letter) + 2])
            else:
                new_msg.append(letter.swapcase())
        return ''.join(new_msg)
    
    return swap_case(message)
    
    
    
    
    
    
    
    
    
    
    
    
    
