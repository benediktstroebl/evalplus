
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
    # Error handling:
    if number > 1000 or number < 1:
        raise ValueError('Number must be between 1 and 1000')

    # Roman numerals symbols:
    symbols = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }

    # Dictionary comprehension:
    roman_number = {number: symbols.get(number) for number in symbols.keys()}

    roman_number_array = []
    for n in roman_number:
        if number >= n:
            roman_number_array.append(roman_number.get(n))
            number -= n

    return ''.join(roman_number_array
