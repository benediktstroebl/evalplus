
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
    def swap_case(char):
        return chr(ord(char) ^ ord('a') ^ ord('A'))
    
    def insert_case(char):
        if char.lower() in 'aeiou':
            return str((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else: 
            return char
    
    return ''.join(insert_case(swap_case(letter)) for letter in message)
   
    
