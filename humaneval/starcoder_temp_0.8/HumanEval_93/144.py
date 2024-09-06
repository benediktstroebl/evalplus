
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
    encoded = ''
    
    for letter in message:
        if letter.isalpha():
            if letter.lower() in 'aeiou':
                new_letter = list(string.ascii_lowercase)
                new_letter.remove(letter.lower())
                new_letter = ''.join(new_letter)
                encoded += new_letter[(new_letter.index(letter.lower()) + 2) % 26]
            else:
                encoded += letter.upper()
        else:
            encoded += letter
    return encoded

