
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
    new_message = ""
    for char in message:
        if char.islower():
            new_message += char.upper()
        elif char.isupper():
            new_message += char.lower()
        else:
            new_message += char
    vowels = "aeiou"
    for char in new_message:
        if char in vowels:
            index = (vowels.index(char)+2)%len(vowels)
            new_message = new_message.replace(char, vowels[index])
    return new_message
