
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
    swapped_message = ""
    for char in message:
        if char.isalpha():
            # swap case
            swapped_char = chr(ord(char) + 32)
            swapped_message += swapped_char
        elif char == "a" or char == "b" or char == "c" or char == "d" or char == "e" or char == "f" or char == "g" or char == "h" or char == "i" or char == "j" or char == "k" or char == "l" or char == "m" or char == "n" or char == "o" or char == "p" or char == "q" or char == "r" or char == "s" or char == "t" or char == "u" or char == "v" or char == "w" or char == "x" or char == "y" or char == "z":
            swapped_message += chr(ord(char) + 10 + 32)
        else:
            swapped_message += char
    return swapped_message
