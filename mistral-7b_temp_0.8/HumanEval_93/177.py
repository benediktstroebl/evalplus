
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
    def convert_vowel(letter):
        if letter.lower() in 'aeiou':
            vowel = ord(letter)
            vowel += 2
            if vowel > ord('z'):
                vowel = ord('a')
            return chr(vowel)
        else:
            return letter

    def convert_case(letter):
        if letter.isupper():
            return letter.lower()
        if letter.islower():
            return letter.upper()

    return ''.join([convert_case(convert_vowel(letter)) for letter in message])

