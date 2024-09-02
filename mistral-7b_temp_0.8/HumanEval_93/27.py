
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
    message = message.upper()
    my_list = list(message)
    my_list = list(map(lambda char: (char if char.isalpha() and char.isupper() else char.lower()), my_list))
    for index, letter in enumerate(my_list):
        if letter.isalpha() and letter.isupper():
            if letter == 'A':
                my_list[index] = 'C'
            elif letter == 'B':
                my_list[index] = 'D'
            elif letter == 'C':
                my_list[index] = 'E'
            elif letter == 'D':
                my_list[index] = 'F'
            elif letter == 'E':
                my_list[index] = 'G'
            elif letter == 'F':
                my_list[index] = 'H'
            elif letter == 'G':
                my_list[index] = 'I'
            elif letter == 'H':
                my_list[index] = 'J'
            elif letter == 'I
