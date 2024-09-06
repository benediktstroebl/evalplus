
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
    def swap_vowel(letter):
        """
        swap_vowel will take a letter, and replace the vowel 
        of the letter with the letter that appears 2 places 
        ahead of that vowel in the english alphabet as long 
        as they are different (whitespace, apostrophe, etc.)
        Examples:
        >>> swap_vowel('t')
        'h'
        >>> swap_vowel('')
        ''
        >>> swap_vowel('X')
        'X'
        """
        if letter == 'a':
            return 'A'
        elif letter == 'o':
            return '0'
        elif letter == 'e':
            return '3'
        elif letter == 'i':
            return '1'
        elif letter == 'u':
            return 'B'
        elif letter == 'A':
            return 'a'
        elif letter == 'O':
            return 'o'
        elif letter == 'E':
            return 'e'
        elif letter == 'I':
            return 'i'
        elif letter == 'U':
            return 'u'
        else:
            return letter
        
    def encode_letter(letter):
        """
        encode_letter will take a letter, and replace it with the 
        letter that appears 2 places ahead of that vowel in the 
        english alphabet as long as they are different (whitespace, 
        apostrophe, etc.)
        Examples:
        >>> encode_letter('t')
        'h'
        >>> encode_letter('')
        ''
        >>> encode_letter('X')
        'X'
        """
        if letter == 'a':
            return 'B'
        elif letter == 'o':
            return '0'
        elif letter == 'e':
            return '3'
        elif letter == 'i':
            return '1'
        elif letter == 'u':
            return '0'
        elif letter == 'A':
            return 'B'
        elif letter == 'O':
            return '0'
        elif letter == 'E':