
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
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    vowels = ['a','e','i','o','u']
    message = message.lower()
    new_message = ''
    for i in range(len(message)):
        if message[i] in alphabet:
            new_message += alphabet[alphabet.index(message[i])+2]
        else:
            new_message += message[i]
    for i in range(len(new_message)):
        if new_message[i] in vowels:
            new_message = new_message[:i] + vowels[vowels.index(new_message[i])].upper() + new_message[i+1:]
    return new_message
