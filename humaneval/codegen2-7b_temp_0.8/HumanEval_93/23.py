
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
    letters = "abcdefghijklmnopqrstuvwxyz"
    new_message = ""
    for char in message:
        if char in letters:
            index = letters.find(char)
            if index + 2 < len(letters):
                new_message += letters[index + 2]
            else:
                new_message += letters[0]
        else:
            new_message += char
    return new_message
