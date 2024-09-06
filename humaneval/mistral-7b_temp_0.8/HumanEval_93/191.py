
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
    output = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet.upper()
    for letter in message:
        if letter in alphabet:
            letter = alphabet.find(letter)
            if letter > 25:
                letter -= 26
            letter += 2
            output += alphabet[letter]
        else:
            output += letter
    return output
