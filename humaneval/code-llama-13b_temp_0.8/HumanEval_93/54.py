
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    message = message.replace(' ', '').lower()
    output = ''
    
    for letter in message:
        if letter in vowels:
            output += chr(ord(letter) + 2)
        else:
            if letter == letter.upper():
                output += chr(ord(letter) + 32)
            else:
                output += letter
    return output
