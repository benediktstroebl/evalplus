
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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    new_message = ""
    for i in message:
        if i in alphabet:
            if i in vowels:
                new_message += alphabet[alphabet.index(i)+2]
            else:
                new_message += i.upper()
        else:
            new_message += i
    return new_message

