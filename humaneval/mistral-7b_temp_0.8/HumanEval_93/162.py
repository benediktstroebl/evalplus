
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
    vowels = "aeiou"
    output = ""
    for letter in message:
        if letter.lower() in vowels:
            if letter.lower() == 'a':
                output += 'c'
            elif letter.lower() == 'e':
                output += 'g'
            elif letter.lower() == 'i':
                output += 'k'
            elif letter.lower() == 'o':
                output += 's'
            elif letter.lower() == 'u':
                output += 'v'
        else:
            output += letter.swapcase()
    return output
