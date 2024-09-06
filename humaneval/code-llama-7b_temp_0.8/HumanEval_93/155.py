
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
    letters = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    for letter in message:
        if letter in letters:
            position = letters.find(letter)
            if letter in vowels:
                position += 2
                if position == 26:
                    position -= 26
            if letter in letters[::-1]:
                position = letters[::-1].find(letter)
                if letter in vowels:
                    position -= 2
                if position == -1:
                    position = 26 - position
            encoded += letters[position]
        else:
            encoded += letter
    return encoded

