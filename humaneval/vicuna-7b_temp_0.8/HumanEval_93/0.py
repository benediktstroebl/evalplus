
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
    message = message.upper()
    encoded = ""
    for char in message:
        if char.isalpha():
            # swap case
            if char.islower():
                encoded += char.upper()
            else:
                encoded += char.lower()
        elif char.isalpha(2):
            # replace vowel with 2 places ahead in alphabet
            index = "AEIOUaeiou".index(char) + 2
            encoded += chr(index)
        else:
            encoded += char
    return encoded