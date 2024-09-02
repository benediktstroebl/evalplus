
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
    res = []
    if number < 1 or number > 1000:
        raise ValueError('Restrictions: 1 <= num <= 1000')
    for num in range(1, number + 1):
        if num <= 1000:
            value = int(num / 1000)
            if value == 1:
                res.append('m')
            else:
                res.append('m' * value)
        if num % 1000 < 100:
            res.append(num % 1000)
    return ''.join(res).lower
