
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
    number = abs(int(number))
    if number > 1000:
        raise ValueError('number must be 1 <= num <= 1000')
    if number < 1:
        raise ValueError('number must be 1 <= num <= 1000')

    m = 'M'
    c = 'C'
    x = 'X'
    v = 'V'
    d = 'D'

    return m * number + c * (number // 100) + x * (number // 10 % 10) + v * (number % 10
