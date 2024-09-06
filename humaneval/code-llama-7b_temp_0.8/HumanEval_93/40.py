
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

    # Using list comprehension to get a list of the vowels
    vowels = [i for i in message if i in 'aeiou']

    # Get the index of the vowels
    vowels_index = [message.index(i) for i in vowels]

    # Replace vowels with the next vowel in the alphabet
    for i in vowels_index:
        message = message[:i] + message[i].lower() + message[i+1].upper() + message[i+2:]

    # Return the encoded message
    return message

