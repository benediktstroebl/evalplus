
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
    for char in message:
        if char.islower():
            char = char.upper()
        elif char.isupper():
            char = char.lower()

        if char == "a":
            char = "c"
        elif char == "c":
            char = "e"
        elif char == "e":
            char = "g"
        elif char == "g":
            char = "i"
        elif char == "i":
            char = "k"
        elif char == "k":
            char = "m"
        elif char == "m":
            char = "o"
        elif char == "o":
            char = "q"
        elif char == "q":
            char = "s"
        elif char == "s":
            char = "u"
        elif char == "u":
            char = "w"
        elif char == "w":
            char = "y"
        elif char == "y":
            char = "a"
        encoded_message += char
    
    return encoded_message
