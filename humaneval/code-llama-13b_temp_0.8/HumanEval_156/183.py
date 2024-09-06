
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
    numerals = {
        '1': 'i',
        '5': 'v',
        '10': 'x',
        '50': 'l',
        '100': 'c',
        '500': 'd',
        '1000': 'm',
    }
    # This is the same as base_to_roman() for base=10.
    res = ''
    for num, char in sorted(numerals.items(), key=lambda x: int(x[0]))[::-1]:
        n = number // int(num)
        number %= int(num)
        if n == 4:
            res += numerals[str(int(num) * 5)] + char * 4
        elif n == 9:
            res += numerals[str(int(num))] + numerals[str(int(num) * 10)]
        else:
            res += char * n
    return res

