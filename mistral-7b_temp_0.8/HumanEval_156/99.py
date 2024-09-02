
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
    """
    >>> int_to_mini_roman(1) == 'i'
    """
    # TODO: write a solution here!
    roman_symbols = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}

    if number < 10:
        return str(number)

    result = ""

    for key in roman_symbols:
        while number >= roman_symbols[key]:
            result += key
            number -= roman_symbols[key]
    return result


