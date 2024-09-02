
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
    # Reference: https://en.wikipedia.org/wiki/Roman_numerals#Modern_usage
    num_map = {
        'm': 1000,
        'd': 500,
        'c': 100,
        'l': 50,
        'x': 10,
        'v': 5,
        'i': 1,
    }

    roman = ''
    for letter, value in num_map.items():
        while number >= value:
            roman += letter
            number -= value

    return roman

