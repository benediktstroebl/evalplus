
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

    # Your code here
    if number < 0:
        return None

    roman_dict = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    roman_representation = ""

    while number > 0:
        for i in range(len(roman_dict.keys())):
            if number - roman_dict[10 ** i] >= 0:
                roman_representation += roman_dict[10 ** i]
                number -= roman_dict[10 ** i]
                break
    return roman_representation.lower()
