
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
    # Create a dictionary to map vowels to their alphabet positions
    vowels = ['a', 'e', 'i', 'o', 'u']
    alphabet = list(range(26))
    for vowel in vowels:
        alphabet[alphabet.index(vowel)] += 2
    
    # Convert message to list of characters
    message_list = list(message)
    
    # Translate vowels to their new positions
    message_list = [chr(ord(c) + 2) for c in message_list]
    
    # Encode message
    return ''.join(message_list)
