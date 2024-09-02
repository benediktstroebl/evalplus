
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
    message = message.replace('a', '2')
    message = message.replace('e', '3')
    message = message.replace('i', '4')
    message = message.replace('o', '5')
    message = message.replace('u', '6')
    message = message.replace('2', 'a')
    message = message.replace('3', 'e')
    message = message.replace('4', 'i')
    message = message.replace('5', 'o')
    message = message.replace('6', 'u')
    message = message.upper()
    message = message.replace('A', '2')
    message = message.replace('E', '3')
    message = message.replace('I', '4')
    message = message.replace('O', '5')
    message = message.replace('U', '6')
    message = message.replace('2', 'A')
    message = message.replace('3', 'E')
    message = message.replace('4', 'I')
    message = message.replace('5', 'O')
    message = message.replace('6', 'U')
    return message
