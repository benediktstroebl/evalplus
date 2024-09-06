

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

    # if the input is a space or nothing, return that
    if not text:
        return ""

    # split the text into a list of characters
    list_text = list(text)

    # iterate through the list of characters
    for index, value in enumerate(list_text):

        # if the character is a vowel, remove it
        if value in vowels:
            list_text[index] = ""

    # return the text joined together
    return "".join(list_text)

