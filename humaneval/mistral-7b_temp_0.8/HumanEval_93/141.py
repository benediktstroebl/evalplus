
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

    # your code here

    vowels = "aeiou"
    message = message.lower()
    new_message = ""
    for x in message:
        if x in vowels:
            new_message += chr(ord(x) + 2)
        else:
            if ord(x) >= 97 and ord(x) <= 122:
                new_message += chr(ord(x) - 32)
            else:
                new_message += x
    return new_message

