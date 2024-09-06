
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
    vowels = "aeiou"
    new_message = []
    for letter in message:
        if letter in vowels:
            ind = vowels.index(letter)
            new_letter = vowels[(ind+2) % 5]
            if letter.isupper():
                new_letter = new_letter.upper()
            new_message.append(new_letter)
        elif letter.isupper():
            new_message.append(letter.lower())
        else:
            new_message.append(letter.upper())
    return ''.join(new_message)
