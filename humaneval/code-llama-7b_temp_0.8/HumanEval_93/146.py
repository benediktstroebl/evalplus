
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
    for letter in message:
        if letter.isupper():
            encoded_message += letter.lower()
        elif letter.islower():
            encoded_message += letter.upper()
        elif letter in ["a", "e", "i", "o", "u"]:
            if letter == "a":
                encoded_message += "D"
            elif letter == "e":
                encoded_message += "T"
            elif letter == "i":
                encoded_message += "B"
            elif letter == "o":
                encoded_message += "P"
            elif letter == "u":
                encoded_message += "G"

    return encoded_message

