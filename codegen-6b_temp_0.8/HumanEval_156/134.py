
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    if not isinstance(number, int):
        raise TypeError("int_to_mini_roman() accepts only integers")
    if not (1 <= number <= 10 ** 4):
        raise ValueError("int_to_mini_roman() accepts only numbers between 1 and 10,000")

    roman_numerals = [
        "",
        "i",
        "ii",
        "iii",
        "iv",
        "v",
        "vi",
        "vii",
        "viii",
        "ix",
    ]

    result = ""
    for i, v in enumerate(reversed(str(number))):
        if i + 1 == len(str(number)) or int(v) < int(str(number)[i + 1]):
            result += roman_numerals[int(v)]

    return result.lower()

