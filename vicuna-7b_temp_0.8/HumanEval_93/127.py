
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
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabetsquared = alphabet + alphabet
    message = [letter.lower() for letter in message]
    for i in range(len(message)-1):
        for j in range(i+1, len(message)):
            if message[i] == message[j] or message[i].isalpha() and message[j].isalpha():
                message[i:j+1] = alphabet + message[i:j+1]
                message[j-1:i] = message[j-1:i] + alphabetsquared[ord(message[j])-ord(message[i])-1]
    return message
