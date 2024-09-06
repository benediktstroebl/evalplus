
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
    vowels_dict = {
        'a': 'c',
        'e': 'g',
        'i': 'i',
        'o': 'k',
        'u': 'm'
    }
    encoded_message = []
    for letter in message:
        if letter.lower() in vowels:
            if letter.islower():
                encoded_message.append(vowels_dict[letter.lower()])
            else:
                encoded_message.append(vowels_dict[letter.lower()].upper())
        else:
            encoded_message.append(letter)
    return ''.join(encoded_message)
