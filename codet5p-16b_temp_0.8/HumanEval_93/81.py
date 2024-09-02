
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

    
    vowels = ['a','e','i','o','u']
    letter_map = {'a':'A', 'e':'E', 'i':'I', 'o':'O', 'u':'U'}

    result = message[:]
    for i in range(len(message)):
        if message[i].lower() in vowels:
            vowel_pos = message[i].lower()
            result = result[:i] + vowel_pos + result[i+1:]
        
        if message[i].lower() in letter_map:
            result = result[:i] + letter_map[message[i].lower()] + result[i+1:]
    return result

