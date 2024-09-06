
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
    encoded_message = []
    for letter in message:
        if letter.islower():
            letter = letter.upper()
        else:
            letter = letter.lower()
        
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            letter = chr(ord(letter) + 2)

        encoded_message.append(letter)

    return ''.join(encoded_message)

