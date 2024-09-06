
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
        raise TypeError('"number" must be an integer')

    if not 1 <= number <= 1000:
        raise ValueError('"number" must be >= 1 and <= 1000')

    roman_nums = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman_num = ''

    for i in range(len(roman_nums)):
        while number >= values[i]:
            roman_num += roman_nums[i]
            number -= values[i]

    return roman_num
