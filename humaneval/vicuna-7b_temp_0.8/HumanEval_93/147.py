
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
    message = message.upper() # converting message to uppercase
    message = message.translate(str.maketrans('aeiou', 'aeiouy')) # swapping cases of letters
    message = message.replace('a', '4') # replacing 'a' with '4'
    message = message.replace('b', '5') # replacing 'b' with '5'
    message = message.replace('c', '6') # replacing 'c' with '6'
    message = message.replace('d', '7') # replacing 'd' with '7'
    message = message.replace('e', '8') # replacing 'e' with '8'
    message = message.replace('f', '9') # replacing 'f' with '9'
    message = message.replace('g', '10') # replacing 'g' with '10'
    message = message.replace('h', '11') # replacing 'h' with '11'
    message = message.replace('i', '12') # replacing 'i' with '12'
    message = message.replace('i', '12') # replacing 'i' with '12'
    message = message.replace('o', '13') # replacing 'o' with '13'
    message = message.replace('p', '14') # replacing 'p' with '14'
    message = message.replace('q', '15') # replacing 'q' with '15'
    message = message.replace('r', '16') # replacing 'r' with '16'
    message = message.replace('s', '17') # replacing 's' with '17'
    message = message.replace('t', '18') # replacing 't' with '18'
    message = message.replace('u', '19') # replacing 'u' with '19'
    message = message.replace('v', '20') # replacing 'v' with '20'
    message = message.replace('w', '21') # replacing 'w' with '21'
    message = message.replace('x', '22') # replacing 'x' with '22'
