
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
    # Your code here
    # print(message)
    # print(message.upper())
    # print(message.lower())
    # print(message.upper()[:5])
    # print(message.lower()[:5])
    # print(message.upper()[:5].lower())
    # print(message.upper()[:5].lower()[:5])
    # print(message.upper()[:5].lower()[:5].upper())
    # print(message.upper()[:5].lower()[:5].upper()[:5])
    # print(message.upper()[:5].lower()[:5].upper()[:5].lower())
    # print(message.upper()[:5].lower()[:5].upper()[:5].lower()[:5])
    # print(message.upper()[:5].lower()[:5].upper()[:5].lower()[:5].upper())

    encode_message = []
    for letter in message:
        #print(letter)
        if letter.upper() in ['A', 'E', 'I', 'O', 'U', 'Y']:
