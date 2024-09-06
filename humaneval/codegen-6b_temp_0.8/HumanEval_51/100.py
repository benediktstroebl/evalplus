

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
    return ''.join([l for l in text if l not in 'aeiouAEIOU'])

    """
    Write a function that accepts a string and returns the string with vowels removed.

    remove_vowels('cabc') #=> 'bc'
    remove_vowels('karaca') #=> 'kca'
    remove_vowels('cab') #=> 'b'
    remove_vowels('') #=> ''
    remove_vowels('This is a string with vowels! It will be vowel removed!') #=> ' is a string with vowels! It will be vowel removed!
    remove_vowels('This is a string with vowels! It will be vowel removed!') #=> ' is a string with vowels! It will be vowel removed!
    """
