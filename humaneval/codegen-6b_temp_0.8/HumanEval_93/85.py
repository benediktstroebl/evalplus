
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
    # code here
    vowels = {"a", "e", "i", "o", "u"}
    letter_index = 0
    message = message.lower()
    out = []
    for char in message:
        if char in vowels:
            letter_index = get_letter_index(char, vowels)
            out.append(get_letter_after_index(letter_index, vowels))
        else:
            out.append(char)
    return "".join(out)

