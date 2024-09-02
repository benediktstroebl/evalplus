
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
    for char in message:
        if char.isalpha():
            if char.islower():
                new_message += char.upper()
            elif char.isupper():
                new_message += char.lower()
            if char in vowels:
                if char == 'a':
                    new_message += 'e'
                elif char == 'e':
                    new_message += 'i'
                elif char == 'i':
                    new_message += 'o'
                elif char == 'o':
                    new_message += 'u'
                else:
                    new_message += 'a'
        else:
            new_message += char
    return new_message
