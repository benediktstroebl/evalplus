

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
    removed_vowels = []
    for letter in text:
        if letter in 'aeiouyAEIOUY':
            continue
        else:
            removed_vowels.append(letter)
    removed_vowels = ''.join(removed_vowels)
    return removed_vowels

