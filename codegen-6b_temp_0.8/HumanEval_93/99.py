
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
    
    def encoder(letter):
        """
        >>> encoder('E')
        'T'

        >>> encoder('a')
        'a'

        >>> encoder('B')
        'c'

        >>> encoder('Z')
        'z'
        """
        vowel_values = ['a', 'e', 'i', 'o', 'u']
        letter_value = ord(letter)
        if letter_value > 64 and letter_value < 91:
            return chr(letter_value)
        elif letter == 'z':
            return 'z'
        elif letter == 'Z':
            return 'Z'
        elif letter == ' ':
            return ' '
        elif letter in vowel_values:
            return vowel_values[(vowel_values.index(letter) + 2) % 5]
        else:
            return letter
    
    return ''.join([encoder(letter) for letter in message.lower()])