
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
    if not isinstance(number, int) or not 1 <= number <= 1000:
        raise ValueError('Number must be between 1 and 1000')

    romans = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    result = []
    for i, r in enumerate(romans):
        result.append(number // r * r)
        number %= r

    return ''.join(
        ['i' * x for x in reversed(result)]
    )

