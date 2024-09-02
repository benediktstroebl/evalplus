

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
    letters = {}
    new_text = ""
    for letter in text:
        letters[letter] = None
    for letter in letters:
        if letter in 'aeiou':
            letters.pop(letter)
    for letter in text:
        if letter in letters:
            new_text += letter
    return new_text



