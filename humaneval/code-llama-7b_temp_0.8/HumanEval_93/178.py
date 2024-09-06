
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

    # The string to be encoded 
    # message = 'This is a message'

    # Swap case of all letters 
    encoded_message = ''
    for char in message: 
        if char.isalpha():
            if char.isupper():
                encoded_message += char.lower()
            else:
                encoded_message += char.upper()
        else:
            encoded_message += char

    # Replace vowels with 2 places ahead of them
    encoded_message = encoded_message.replace('A', 'C')
    encoded_message = encoded_message.replace('a', 'c')
    encoded_message = encoded_message.replace('E', 'G')
    encoded_message = encoded_message.replace('e', 'g')
    encoded_message = encoded_message.replace('I', 'K')
    encoded_message = encoded_message.replace('i', 'k')
    encoded_message = encoded_message.replace('O', 'N')
    encoded_message = encoded_message.replace('o', 'n')
    encoded_message = encoded_message.replace('U', 'R')
    encoded_message = encoded_message.replace('u', 'r')

    # The encoded message
    print(encoded_message)



