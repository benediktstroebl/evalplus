
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
    encoded_message = ""
    index_vowels = "AEIOUaeiou"
    index_2_ahead_vowels = "GJPRBZNKQMgjprbznkmq"
    for i in message:
        if i in index_vowels:
            index = index_vowels.index(i)
            encoded_message += index_2_ahead_vowels[index]
        elif i in index_2_ahead_vowels:
            index = index_2_ahead_vowels.index(i)
            encoded_message += index_vowels[index]
        else:
            encoded_message += i.swapcase()
    return encoded_message
