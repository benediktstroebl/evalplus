
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
    encoded_message = ""
    vowels = "aeiou"
    for char in message:
        if char.isalpha():
            if char.isupper():
                new_char = chr(ord(char) + 2)
                if new_char in vowels:
                    new_char = new_char.lower()
                encoded_message += new_char
            elif char.islower():
                new_char = chr(ord(char) + 2)
                if new_char in vowels:
                    new_char = new_char.lower()
                encoded_message += new_char.upper()
        else:
            encoded_message += char
    return encoded_message
