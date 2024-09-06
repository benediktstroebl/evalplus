
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
    new_message = ''
    for letter in message:
        if letter.lower() == 'a':
            new_message += 'C'
        elif letter.lower() == 'b':
            new_message += 'D'
        elif letter.lower() == 'c':
            new_message += 'E'
        elif letter.lower() == 'd':
            new_message += 'F'
        elif letter.lower() == 'e':
            new_message += 'G'
        elif letter.lower() == 'f':
            new_message += 'H'
        elif letter.lower() == 'g':
            new_message += 'I'
        elif letter.lower() == 'h':
            new_message += 'J'
        elif letter.lower() == 'i':
            new_message += 'K'
        elif letter.lower() == 'j':
            new_message += 'L'
        elif letter.lower() == 'k':
            new_message += 'M'
        elif letter.lower() == 'l':
            new_message += 'N'
        elif letter.lower() == 'm':
            new_message += 'O'
        elif letter.lower() == 'n':
            new_message += 'P'
        elif letter.lower() == 'o':
            new_message += 'Q'
        elif letter.lower() == 'p':
            new_message += 'R'
        elif letter.lower() == 'q':
            new_message += 'S'
        elif letter.lower() == 'r':
            new_message += 'T'
        elif letter.lower() == 's':
            new_message += 'U'
        elif letter.lower() == 't':
            new_message += 'V'
        elif letter.lower() == 'u':
            new_message += 'W'
        elif letter.lower() == 'v':
            new_message += 'X'
        elif letter.lower() == 'w':
            new_message += 'Y'
        elif letter.lower() == 'x':
            new_message += 'Z'
        elif letter.lower() == 'y':
            new_message += 'A
