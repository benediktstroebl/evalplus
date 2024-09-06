
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
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    encoded_message = ''
    for i in message:
        if i in vowels:
            new_letter = message[message.find(i)+2]
            encoded_message += new_letter
        else:
            encoded_message += i.lower()
    return encoded_message


