
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
    vowels = 'aeiou'
    new_message = ''
    for letter in message:
        if letter.islower():
            new_letter = letter.upper()
        else:
            new_letter = letter.lower()
        if new_letter in vowels:
            index = vowels.find(new_letter) + 2
            if index > 5:
                index = index - 5
            new_letter = vowels[index]
        new_message = new_message + new_letter
    return new_message
