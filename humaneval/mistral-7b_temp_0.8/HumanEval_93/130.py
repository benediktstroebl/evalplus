
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
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = lower_case.upper()
    vowels = 'aeiou'
    new_message = ""
    for char in message:
        if char.isalpha():
            if char.upper() in upper_case:
                new_message += char.lower()
            elif char.lower() in lower_case:
                new_message += char.upper()
            else:
                new_message += char
        elif char == ' ':
            new_message += char
        else:
            pass
    for char in new_message:
        if char in vowels:
            char_index = vowels.index(char)
            new_char = vowels[char_index+2]
            new_message = new_message.replace(char, new_char)
    return new_message

