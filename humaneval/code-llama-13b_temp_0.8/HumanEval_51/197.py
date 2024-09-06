

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

    # make a list of all the letters of the alphabet and vowels
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    vowels = ["a", "e", "i", "o", "u"]
    
    # check if text is not empty
    if len(text) != 0:
        
        # loop through the string
        for x in text:
            
            # check if the letter is a vowel
            if x in vowels:

                # remove it
                text = text.replace(x, "")

    # return the result
    return text
