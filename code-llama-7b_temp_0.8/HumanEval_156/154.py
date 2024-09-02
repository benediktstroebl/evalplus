
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

    # make sure the number is greater than 0
    if number < 1:
        raise ValueError('number must be greater than zero')
    if number > 1000:
        raise ValueError('number must be less than 1000')

    # roman numerals are based on powers of 10, so we want to start with the largest number
    # smaller than the number provided, and work our way down
    roman_nums = (
        (1000, 'm'),
        (900, 'cm'),
        (500, 'd'),
        (400, 'cd'),
        (100, 'c'),
        (90, 'xc'),
        (50, 'l'),
        (40, 'xl'),
        (10, 'x'),
        (9, 'ix'),
        (5, 'v'),
        (4, 'iv'),
        (1, 'i')
    )
    result = ''
    for num, letter in roman_nums:
        while number >= num:
            result += letter
            number -= num
    return result.lower()
