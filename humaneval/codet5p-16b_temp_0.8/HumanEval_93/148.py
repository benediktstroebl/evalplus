
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

    message = message.lower()
    vowels = 'aeiou'
    
    new_message = ''
    for letter in message:
        if letter in vowels:
            if message.index(letter) == 0:
                new_message += 'a'
            elif message.index(letter) == 1:
                new_message += 'b'
            elif message.index(letter) == 2:
                new_message += 'c'
            elif message.index(letter) == 3:
                new_message += 'd'
            elif message.index(letter) == 4:
                new_message += 'e'
            elif message.index(letter) == 5:
                new_message += 'f'
            elif message.index(letter) == 6:
                new_message += 'g'
            elif message.index(letter) == 7:
                new_message += 'h'
            elif message.index(letter) == 8:
                new_message += 'i'
            elif message.index(letter) == 9:
                new_
