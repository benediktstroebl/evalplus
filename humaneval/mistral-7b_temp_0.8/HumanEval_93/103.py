
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
    final = ""
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                final += ch.lower()
            else:
                final += ch.upper()
        else:
            final += ch
    vowels = "AEIOU"
    for i in range(len(message)):
        if message[i] in vowels:
            final = final[:i] + chr(ord(message[i])+2) + final[i+1:]
    return final
