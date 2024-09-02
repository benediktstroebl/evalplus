
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
    assert type(number) == int, 'number must be an integer'
    assert number >= 1 and number <= 1000, 'number must be between 1 and 1000'
    result = []
    keys = ['', 'm', 'c', 'x', 'i', 'v', 'l', 'd']
    values = ['', 'm', 'c', 'x', 'i', 'v', 'l', 'd']
    for i in range(len(keys)):
        while number >= values[i]:
            result.append(keys[i])
            number -= values[i]
    return ''.join(result)

