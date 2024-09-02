
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

    if 1 <= number <= 1000:
        romans = ['i', 'v', 'x', 'l', 'c', 'd','m']
        result = ''
        for i in range(len(romans)):
            count = number // (10 ** (len(romans) - i - 1))
            result += romans[i] * count
            number -= count * (10 ** (len(romans) - i - 1))
        return result.lower()
    else:
        raise ValueError('Restrictions: 1 <= num <= 1000')
