
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
    result = ""
    for letter in message:
        if letter.lower() == 'a':
            result += 'C'
        if letter.lower() == 'b':
            result += 'D'
        if letter.lower() == 'c':
            result += 'E'
        if letter.lower() == 'd':
            result += 'F'
        if letter.lower() == 'e':
            result += 'G'
        if letter.lower() == 'f':
            result += 'H'
        if letter.lower() == 'g':
            result += 'I'
        if letter.lower() == 'h':
            result += 'J'
        if letter.lower() == 'i':
            result += 'K'
        if letter.lower() == 'j':
            result += 'L'
        if letter.lower() == 'k':
            result += 'M'
        if letter.lower() == 'l':
            result += 'N'
        if letter.lower() == 'm':
            result += 'O'
        if letter.lower() == 'n':
            result += 'P'
        if letter.lower() == 'o':
            result += 'Q'
        if letter.lower() == 'p':
            result += 'R'
        if letter.lower() == 'q':
            result += 'S'
        if letter.lower() == 'r':
            result += 'T'
        if letter.lower() == 's':
            result += 'U'
        if letter.lower() == 't':
            result += 'V'
        if letter.lower() == 'u':
            result += 'W'
        if letter.lower() == 'v':
            result += 'X'
        if letter.lower() == 'w':
            result += 'Y'
        if letter.lower() == 'x':
            result += 'Z'
        if letter.lower() == 'y':
            result += 'A'
        if letter.lower() == 'z':
            result += 'B'
        if letter.isupper():
            result += letter.swapcase()
        if letter.lower() not in 'abcdefghijklmn
