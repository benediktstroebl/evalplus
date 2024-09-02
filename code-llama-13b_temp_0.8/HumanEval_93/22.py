
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
    new_message = []
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    shift = 2
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                new_message.append(uppercase[uppercase.index(letter) + shift])
            else:
                new_message.append(lowercase[lowercase.index(letter) + shift])
        else:
            new_message.append(letter)
    return ''.join(new_message)
    
    
