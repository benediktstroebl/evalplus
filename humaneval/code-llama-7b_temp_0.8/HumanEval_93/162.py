
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    message = message.lower()
    new_message = ''

    for index, letter in enumerate(message):
        if letter in vowels:
            vowels_index = vowels.index(letter)
            vowels_index = vowels_index + 2
            if vowels_index > 4:
                vowels_index = vowels_index - 5
            new_letter = vowels[vowels_index]
        else:
            new_letter = letter
        if index % 2 == 0:
            new_message += new_letter.upper()
        else:
            new_message += new_letter
    return new_message
