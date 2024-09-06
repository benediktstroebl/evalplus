
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
    vowels_dict = {'a': 'c', 'e': 'g', 'i': 'i', 'o': 'k', 'u': 'm'}
    
    encoded_message = ''
    for letter in message:
        if letter.isalpha() == True:
            if letter.islower() == True:
                letter = letter.upper()
            if letter in vowels:
                index = (vowels.index(letter) + 2) % 5
                letter = vowels[index]
            else:
                letter = letter.lower()
            encoded_message += letter
        else:
            encoded_message += letter
    return encoded_message

