
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
    def get_idx(letter):
        try:
            return alphabet.index(letter.lower())
        except ValueError:
            return None
    def encode_pair(letter):
        idx = get_idx(letter)
        if idx is None:
            return letter
        else:
            return alphabet[idx+2]
    switch_capital = str.maketrans(
        str.maketrans('aeiou', 'CDEFG'),
        str.maketrans('AEIOU', 'CGDFG'))
    return ''.join(encode_pair(letter)
                   .translate(switch_capital)
                   .upper()
                   for letter in message)
