
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
    
    if not isinstance(message, str) or len(message) < 1:
        raise ValueError('Message should be a nonempty string')
    
    def swap_case(ch):
        if ord(ch) >= 97 and ord(ch) <= 122:
            return chr(ord(ch) - 32)
        elif ord(ch) >= 65 and ord(ch) <= 90:
            return chr(ord(ch) + 32)
        else:
            return ch
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(message)):
        if message[i].lower() in vowels:
            message = message[:i] + swap_case(message[i]) + message[i + 1:]
            
    return message

