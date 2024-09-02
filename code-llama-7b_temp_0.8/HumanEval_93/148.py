
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
    #String to list conversion
    x=list(message)

    #Function to make vowels to uppercase and swap them with 2 places ahead of that vowel in alphabet
    for i in range(len(x)):
        if x[i] == 'a':
            x[i] = 'B'
        elif x[i] == 'e':
            x[i] = 'F'
        elif x[i] == 'i':
            x[i] = 'H'
        elif x[i] == 'o':
            x[i] = 'J'
        elif x[i] == 'u':
            x[i] = 'N'
        elif x[i] == 'A':
            x[i] = 'B'
        elif x[i] == 'E':
            x[i] = 'F'
        elif x[i] == 'I':
            x[i] = 'H'
        elif x[i] == 'O':
            x[i] = 'J'
        elif x[i] == 'U':
            x[i] = 'N'

    #Making all the alphabets except vowels to lowercase
    for i in range(len(x)):
        if x[i] == 'B':
            x[i] = 'A'
        elif x[i] == 'F':
            x[i] = 'E'
        elif x[i] == 'H':
            x[i] = 'I'
        elif x[i] == 'J':
            x[i] = 'O'
        elif x[i] == 'N':
            x[i] = 'U'

    #List to string conversion
    return "".join(x)
