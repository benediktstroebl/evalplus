
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
    alpha = "abcdefghijklmnopqrstuvwxyz"
    new_msg = ""
    for letter in message.lower():
        if letter in alpha:
            if letter in "aeiou":
                new_msg += alpha[(alpha.index(letter)+2)%26]
            else:
                new_msg += letter.swapcase()
        else:
            new_msg += letter
    return new_msg
    
