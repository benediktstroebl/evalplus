
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
    if not isinstance(number, int) or not isinstance(number, int):
        raise TypeError
    if number < 1 or number > 1000:
        raise ValueError
    if number < 1000:
        return int_to_roman(number)
    else:
        return int_to_roman(number // 1000) + 'x' * (number % 1000 // 100) + int_to_roman(number % 100
