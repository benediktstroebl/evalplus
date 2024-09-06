

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
    # We need a base case to terminate the recursion.
    if text == '':
        return ''

    # We check if the first letter is a vowel.
    # If it is, we don't include it in the result.
    # We then call the function recursively for the remaining part of the string.
    # If the first letter is not a vowel, we include it in the result.
    if text[0].lower() in "aeiou":
        return remove_vowels(text[1:])
    else:
        return text[0] + remove_vowels(text[1:])

