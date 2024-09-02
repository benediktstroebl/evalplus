
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
    vowels = "aeiouAEIOU"
    result = ""
    for letter in message:
        if letter.lower() in vowels:
            result += letter.upper()
        else:
            index = ord(letter.lower()) - ord('a')
            result += chr((ord(letter.lower()) - ord('a') + 2) % 26)
    return result
