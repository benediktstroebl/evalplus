
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
    #create a dictionary of letters and their replacements
    alphabet = {
        'a':'c',
        'b':'d',
        'c':'e',
        'd':'f',
        'e':'g',
        'f':'h',
        'g':'i',
        'h':'j',
        'i':'k',
        'j':'l',
        'k':'m',
        'l':'n',
        'm':'o',
        'n':'p',
        'o':'q',
        'p':'r',
        'q':'s',
        'r':'t',
        's':'u',
        't':'v',
        'u':'w',
        'v':'x',
        'w':'y',
        'x':'z',
        'y':'a',
        'z':'b'
    }

    #create a list of vowels
    vowels = 'aeiou'

    #create an empty string to store the encoded message
    encoded_message = ''

    #for each letter in the message:
    for letter in message.lower():
        #if the letter is a vowel:
        if letter in vowels:
            #add the letter from the alphabet dictionary that is 2 places ahead of the vowel
            encoded_message = encoded_message + alphabet[letter]
        #otherwise:
        else:
            #add the letter in lowercase
            encoded_message = encoded_message + letter

    #return the encoded message
    return encoded_message.upper()
