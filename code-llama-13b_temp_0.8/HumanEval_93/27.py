
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
    encoded_message = ''
    vowels = ['a','e','i','o','u']
    for letter in message:
        if letter in vowels:
            new_letter = chr(ord(letter)+2)
            if new_letter in vowels:
                new_letter = chr(ord(new_letter)+2)
            encoded_message += new_letter
        elif letter == ' ':
            encoded_message += ' '
        else:
            encoded_message += letter.swapcase()
    return encoded_message
            
            
