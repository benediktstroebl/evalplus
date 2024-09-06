
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
    # Your code here
    output = ""
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                output += letter.upper()
            else:
                output += letter.lower()
        elif letter == "a":
            output += "c"
        elif letter == "e":
            output += "g"
        elif letter == "i":
            output += "k"
        elif letter == "o":
            output += "q"
        elif letter == "u":
            output += "w"
        else:
            output += letter
    return output

