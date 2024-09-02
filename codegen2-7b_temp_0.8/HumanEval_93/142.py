
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
    vowel_list = ['A', 'E', 'I', 'O', 'U', 'Y']
    message = message.upper()
    for letter in message:
        if letter in vowel_list:
            position = vowel_list.index(letter)
            letter = message[position+2]
        else:
            letter = letter
    return
