
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
    new_message = []
    for char in message:
        if char in 'AEIOUaeiou':
            char = char.upper()
            char_index = ord(char) - ord('A')
            char_index *= 2
            new_message.append(chr(char_index + ord('A')))
        else:
            new_message.append(char)
    return ''.join(new_message)
