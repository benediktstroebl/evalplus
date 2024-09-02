
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
        raise TypeError('Must pass a positive integer')
    if not 1 <= number <= 1000:
        raise ValueError('Must pass a positive integer up to 1000')

    r = ''

    for i in range(1, 4 + 1):
        num = number
        mod = (num % 10)

        if mod == 4:
            r = 'cd' + r
            num -= 5
        elif mod == 9:
            r = 'cm' + r
            num -= 10

        if mod < 5:
            r = v[mod] + r
        elif mod >= 5:
            r = v[mod % 5] + r
            num -= (mod % 5)

        number -= mod

    return r


assert int_to_mini_roman(19) == 'xix'
assert int_to_mini_roman(152) == 'clii'
assert int_to_mini_roman(426) == 'cdxxvi'
assert int_to_mini_roman(567) == 'cdxlx'
