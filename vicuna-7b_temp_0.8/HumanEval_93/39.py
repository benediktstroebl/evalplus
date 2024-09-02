
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
    message = message.upper() # convert to upper case
    # convert to lower case internally
    message = message.lower()
    result = ""
    for char in message:
        if char.isalpha():
            # check if this is a vowel
            if char.isupper():
                # if it is upper case, look 2 places ahead in the alphabet
                next_letter = "".join(chr(ord("A") + (ord(char) - ord("A")) % 26 + 1) for _ in range(2))
            else:
                next_letter = chr(ord(char) + 1)
            result += next_letter
        else:
            result += char
    return result.replace(" ", "_")
