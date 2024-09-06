
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
    # Convert message to a list of characters
    message = list(message)
    
    # Step 1: swap case
    message = message[::-1]
    
    # Step 2: replace vowels with their next letter in alphabet
    message = [ord(letter) - ord('A') for letter in message]
    
    return ''.join(message)
