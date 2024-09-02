

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

    # if the input is empty or just contains vowels
    if not text or len(text) == len(text.lower().replace('a', '')):
        return ''

    # create a variable to hold the output
    output = ''

    # for each character in the input
    for char in text:
        # if the character is not a vowel
        if char not in 'aeiouAEIOU':
            # add it to the output
            output += char

    # return the output
    return output

