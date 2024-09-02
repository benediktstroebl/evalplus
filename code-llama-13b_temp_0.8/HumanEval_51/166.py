

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
    vowels = "aeiou"
    vowels += vowels.upper()

    def remove(text):
        new_text = ""
        for character in text:
            if character not in vowels:
                new_text += character
        return new_text

    return "\n".join(remove(line) for line in text.splitlines())

