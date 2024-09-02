
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
    def swap_case(letter):
        if letter.isupper():
            return letter.lower()
        else:
            return letter.upper()

    def replace_vowel(vowel):
        vowels = ['a', 'e', 'i', 'o', 'u']
        index = vowels.index(vowel) + 2
        return vowels[index]

    encoded = ""
    for letter in message:
        encoded += replace_vowel(letter) if letter in vowels else swap_case(letter)
    return encoded

