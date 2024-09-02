
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
    vowels = ["a","e","i","o","u"]
    replaced_message = []
    for char in message:
        if char.lower() in vowels:
            replaced_message.append(encode_vowel(char))
        else:
            replaced_message.append(char)
    return "".join(replaced_message)

