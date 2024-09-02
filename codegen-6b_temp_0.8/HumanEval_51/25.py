

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
    letter_list = list(text)
    for ele in letter_list:
        if ele in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            letter_list.remove(ele)
    return ''.join(letter_list)

text = 'bcd\nabc\na'