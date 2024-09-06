
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
    
    # To be able to handle both lower case as well as upper case letters
    # and vowels, we first convert the message to lower case.
    message = message.lower()

    # We then convert the message into a list for convenience.
    message_list = list(message)

    for i in range(len(message_list)):
        # Based upon the length of the message, we find the position of
        # the vowel in the list. Vowels can be added, but we first check
        # if the current position is the first vowel, if it is, we skip it.
        if VOWEL.isalpha(message_list[i]):
            if i == 0:
                continue
            
            # Then we find the alphabet position of the vowel.
            # Note that the vowels can be added to the message, but we use
            # the previous vowel to check for a position instead of the current
            # vowel.
            n = alphabet.index(message_list[i-1])
            message_list[i] = alphabet[n+2]

    return ''.join(message_list)