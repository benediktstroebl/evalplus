
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
    roman_map = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }

    def _int_to_roman(n):
        if n <= 0:
            raise ValueError('Number must be positive.')
        elif n == 1000:
            return 'm'
        elif n > 1000:
            return _int_to_roman(n // 1000) + roman_map[1000] + \
                _int_to_roman(n % 1000)
        elif n in roman_map:
            return roman_map[n]
        else:
            for i, digit in enumerate(reversed(list(str(n)))):
                for x in range(int(digit), 0, -1):
                    yield roman_map[10 ** i * x]

    return ''.join(_int_to_roman(number))
