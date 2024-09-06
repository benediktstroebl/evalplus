

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    lowercase_letters = [chr(i) for i in range(97, 123)]
    uppercase_letters = [chr(i) for i in range(65, 91)]
    transliterated = ""
    for char in string:
        if char in lowercase_letters:
            transliterated = transliterated + char.upper()
        elif char in uppercase_letters:
            transliterated = transliterated + char.lower()
        else:
            transliterated = transliterated + char
    return transliterated
