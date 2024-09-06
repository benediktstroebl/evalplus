
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
    encode_case = {ord(char.lower()): ord(char.upper()) for char in 'abcdefghijklmnopqrstuvwxyz'}
    vowel_indices = [ord(char) for char in 'aeiou']
    vowel_indices += vowel_indices
    vowel_indices += vowel_indices
    vowel_indices += vowel_indices
    vowel_indices += vowel_indices
    vowel_indices += vowel_indices
    vowel_indices = [char for char in vowel_indices if char not in vowel_indices[:-3]]
    vowel_indices += [ord('z')]
    vowel_indices = [' '.join(map(chr, indices)) for indices in vowel_indices]
    vowel_replacements = {char: indices[1] for char, indices in zip('aeiou', vowel_indices)}
    return ''.join(map(lambda char: encode_case.get(ord(char), ord(char)),
