

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    # function definition
    def remove_vowels(text):
        """
        This function removes vowels from a given text using a dictionary.
        :param text: str
        :return: str
        """
        # dictionary to store vowels
        vowels = set('aeiouAEIOU')
        
        # convert string to lowercase and remove punctuations
        text = text.lower().replace(' ', '')
        
        # remove vowels
        text = ''.join([c for c in text if c not in vowels])
        
        return text
        
    # calling the function
    return remove_vowels(text)
