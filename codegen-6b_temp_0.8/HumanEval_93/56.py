
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
    #TODO replace "vowels"
    # Todo: add "consonants"

    vowels = 'AEIOU'
    letters = string.ascii_lowercase
    new_message = ''
    
    for letter in message:
        if letter in vowels:
            index = vowels.index(letter)
            new_index = index + 2
            new_letter = vowels[new_index]
        else:
            new_letter = letter
        new_message += new_letter
    return new_message


