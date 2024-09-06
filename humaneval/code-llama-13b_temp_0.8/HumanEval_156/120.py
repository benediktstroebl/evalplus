
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
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }
    powers = list(sorted(numerals.keys(), reverse=True))
    assert all(p < q for p, q in zip(powers[:-1], powers[1:])), powers
    result = ''
    num_left = number
    while powers:
        power = powers.pop(0)
        while num_left >= power:
            num_left -= power
            result += numerals[power]
    return result

