
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
    m = message.lower()
    vowels = set('aeiou')
    a = 'abcdefghijklmnopqrstuvwxyz'
    vowel_index = {c: i for i, c in enumerate(a)}
    new_a = a.swapcase()
    def encode_vowel(letter):
        return new_a[(vowel_index[letter] + 2) % len(new_a)]
    m = ''.join(map(lambda l: encode_vowel(l) if l in vowels else l, m))
    return m
