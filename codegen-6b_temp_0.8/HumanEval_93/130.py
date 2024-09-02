
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
    def find_index(letter):
        #y will be the index of the letter in the VOWELS array
        y=VOWELS.index(letter)
        return y + 2
    
    def encode_vowel(letter):
        x = VOWELS[find_index(letter)]
        return x
    #VOWELS = ['a','e','i','o','u']
    message = message.lower()
    result = []
    for letter in message:
        if letter in VOWELS:
            result.append(encode_vowel(letter))
        else:
            result.append(letter)
    return ''.join(result)
