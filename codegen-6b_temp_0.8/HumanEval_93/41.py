
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
    # Your code goes here
    to_swap = list(message)
    for letter in message:
        if letter.upper() in 'AEIOU':
            to_swap[to_swap.index(letter.upper())] = ascii_letters[(ascii_letters.index(letter.upper())+2)%len(ascii_letters)]
    return ''.join(to_swap)
        


