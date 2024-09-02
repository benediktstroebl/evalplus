
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
    newMessage = ''
    for letter in message:
        if letter.lower() in 'aeiou':
            newMessage += chr((ord(letter) - 97 + 2) % 26 + 97)
        elif letter.islower():
            newMessage += chr((ord(letter) - 97 + 26) % 26 + 97)
        elif letter.isupper():
            newMessage += chr((ord(letter) - 65 + 26) % 26 + 65)
        else:
            newMessage += letter
    return newMessage
