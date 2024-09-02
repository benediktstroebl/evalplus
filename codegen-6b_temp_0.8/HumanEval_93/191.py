
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
    ### 1. Write code here!
    result = ""
    vowels = "AEIOUaeiou"
    for i in message:
        if i.isalpha() and i.upper() not in vowels: #convert to uppercase
            c = i.lower()
            result += (chr(ord(c) + 2))
        elif i.isalpha() and i.upper() in vowels:
            result += chr(ord(i) + 2)
        else:
            result += i
    return result
