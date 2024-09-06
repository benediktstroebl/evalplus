
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

    # YOUR CODE HERE

    #vowels = ['a','e','i','o','u']
    vowels = ['a','e','i','o','u']
    vowels2 = ['b','f','j','l','m','n','p','s','t','v','w','x','y','z']

    message = message.lower()
    encoded_message = ""
    for letter in message:
        if letter in vowels:
            encoded_message += vowels2[vowels.index(letter)]
        else:
            encoded_message += letter.upper()
    return encoded_message
