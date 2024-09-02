
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
    vowels = "aeiou"
    result = ""
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                result += chr(ord(letter.upper()) + 2)
            elif letter.upper() in vowels:
                result += chr(ord(letter.lower()) + 2)
            else:
                result += letter.upper() if letter.isupper() else letter.lower()
        else:
            result += letter
    return result

