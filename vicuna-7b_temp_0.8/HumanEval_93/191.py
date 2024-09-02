
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

message = message.upper()  # convert message to uppercase
message = message.replace("a", "A")  # replace "a" with "A"
message = message.replace("e", "E")  # replace "e" with "E"
message = message.replace("i", "I")  # replace "i" with "I"
message = message.replace("o", "O")  # replace "o" with "O"
message = message.replace("u", "U")  # replace "u" with "U"
message = message.replace("y", "Y")  # replace "y" with "Y"

message = message.split()  # split the message into a list of characters
message = "".join([message[i] if (j == i) else (message[j] if (j < i) else (message[j] + "A")) for i, j in enumerate(message) if (j == "a") or (j == "e") or (j == "i") or (j == "o") or (j == "u")])  # if a vowel appears before a, replace it with that vowel + "A"
