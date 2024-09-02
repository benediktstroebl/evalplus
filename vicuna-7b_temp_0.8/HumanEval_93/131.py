
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
    # split message into a list of characters
    message_list = message.split()
    
    # iterate through each character in the message
    for i, char in enumerate(message_list):
        # if char is a vowel, replace it with a vowel 2 places ahead
        if char.lower() in "aeiou":
            # replace it with a vowel 2 places ahead
            if i + 2 < len(message_list):
                new_char = chr(ord(char) + 2)
            else:
                new_char = chr(ord(char) + 2) + chr(ord(char) + 4)
            message_list[i] = new_char
    
    # join the message back into a string
    return ''.join(message_list)