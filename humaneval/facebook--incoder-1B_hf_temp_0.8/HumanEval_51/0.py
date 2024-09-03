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
    vowels = "AEIOUaeiou"
    chars = text
    count = 0
    vowel_count = 0
    vowel_pos = 0
    while True:
        if chars[vowel_pos] in vowels:
            vowel_count += 1
        else:
            chars = chars.replace(chars[vowel_pos:], "")
            count -= 1
            vowel_pos = 0
            vowel_count -= 1
            if count == 0:
                return chars

