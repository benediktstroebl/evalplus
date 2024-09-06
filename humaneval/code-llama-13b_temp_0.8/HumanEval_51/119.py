

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
    # string_vowels = "aeiou"
    # return "".join(letter for letter in text if letter.lower() not in string_vowels)

    # remove vowels with deque O(N)
    from collections import deque

    text_deque = deque()
    vowels = set("aeiou")
    for letter in text:
        if letter.lower() not in vowels:
            text_deque.append(letter)
    return "".join(text_deque)

