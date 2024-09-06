
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
    def vowel_encode(char):
        if char in "aeiou":
            return chr((ord(char) - 97 + 2) % 26 + 97)
        return char
    
    return message.lower().translate(str.maketrans('aeiou', 'AEIOU')).translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.whitespace)).translate(string.maketrans("".join(string.ascii_lowercase), "".join(string.ascii_lowercase[2:] + string.ascii_lowercase[:2])))
    
    return "".join(map(vowel_encode, message))

