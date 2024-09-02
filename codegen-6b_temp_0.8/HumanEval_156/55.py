
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
    # Initialization
    romans = ['x', 'c', 'm', 'y']
    chars = ['1', '10', '100', '1000']
    result = ''
    while number > 0:
        index = number - 1
        number, remainder = divmod(number, 10)
        result = romans[index] + result
        if remainder >= 5:
            result = romans[index + 1] + result
            number -= 1
    return result.lower()

