
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
    for c in message:
        if c.lower() == 'a':
            encoded += 'D'
        if c.lower() == 'b':
            encoded += 'E'
        if c.lower() == 'c':
            encoded += 'F'
        if c.lower() == 'd':
            encoded += 'G'
        if c.lower() == 'e':
            encoded += 'H'
        if c.lower() == 'f':
            encoded += 'I'
        if c.lower() == 'g':
            encoded += 'J'
        if c.lower() == 'h':
            encoded += 'K'
        if c.lower() == 'i':
            encoded += 'L'
        if c.lower() == 'j':
            encoded += 'M'
        if c.lower() == 'k':
            encoded += 'N'
        if c.lower() == 'l':
            encoded += 'O'
        if c.lower() == 'm':
            encoded += 'P'
        if c.lower() == 'n':
            encoded += 'Q'
        if c.lower() == 'o':
            encoded += 'R'
        if c.lower() == 'p':
            encoded += 'S'
        if c.lower() == 'q':
            encoded += 'T'
        if c.lower() == 'r':
            encoded += 'U'
        if c.lower() == 's':
            encoded += 'V'
        if c.lower() == 't':
            encoded += 'W'
        if c.lower() == 'u':
            encoded += 'X'
        if c.lower() == 'v':
            encoded += 'Y'
        if c.lower() == 'w':
            encoded += 'Z'
        if c.lower() == 'x':
            encoded += 'A'
        if c.lower() == 'y':
            encoded += 'B'
        if c.lower() == 'z':
            encoded += 'C'
        if c.isupper():
            encoded += c.lower()
        if c.islower():
            encoded += c.upper()
