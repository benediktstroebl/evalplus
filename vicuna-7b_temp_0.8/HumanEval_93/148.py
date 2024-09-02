
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
    message = message.upper() # converting message to uppercase
    result = ""
    for char in message:
        if char.isalpha(): # check if only letters are present in the message
            if char.isalpha() and char.isalpha()[1].isalpha(): # if both letters are present, then swap their positions
                if char.isalpha()[1].isalpha() == 'a':
                    if char.isalpha()[0] == 'a':
                        result += chr(ord('a') + 2) + chr(ord(char.isalpha()[1]) - 2)
                    elif char.isalpha()[0] == 'e':
                        result += chr(ord('e') + 2) + chr(ord(char.isalpha()[1]) - 2)
                    elif char.isalpha()[0] == 'i':
                        result += chr(ord('i') + 2) + chr(ord(char.isalpha()[1]) - 2)
                    elif char.isalpha()[0] == 'o':
                        result += chr(ord('o') + 2) + chr(ord(char.isalpha()[1]) - 2)
                    elif char.isalpha()[0] == 'u':
                        result += chr(ord('u') + 2) + chr(ord(char.isalpha()[1]) - 2)
                else:
                    if char.isalpha()[1].isalpha() == 'o':
                        result += chr(ord('o') + 2) + chr(ord(char.isalpha()[1]) - 2)
                    elif char.isalpha()[1].isalpha() == 'u':
                        result += chr(ord('u') + 2) + chr(ord(char.isalpha()[1]) - 2)
                    elif char.isalpha()[1].isalpha() == 'y':
                        result += chr(ord('y') + 2) + chr(ord(char.isalpha()[1]) - 2)
            else:
                result += char
    return result.lower()
