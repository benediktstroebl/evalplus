
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

    # your code here
    # Convert to all lower case, uppercase to lowercase
    message = message.lower()
    # Copy all the message
    tmp = list(message)
    # Encode message
    for i in range(len(message)):
        if message[i] == 'a':
            tmp[i] = 'c'
        if message[i] == 'e':
            tmp[i] = 'g'
        if message[i] == 'i':
            tmp[i] = 'k'
        if message[i] == 'o':
            tmp[i] = 't'
        if message[i] == 'u':
            tmp[i] = 'w'
        if message[i] in 'aeiou':
            tmp[i] = chr(ord(message[i]) + 2)
    # Convert back to string
    message = ''.join(tmp)
    return message.upper()

