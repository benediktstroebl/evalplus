
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
    assert type(number) == int
    assert 1 <= number <= 1000
    result = ""
    roman = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    for i in range(len(str(number)), 0, -1):
        digit = number // (10 ** (i - 1))
        result += roman[digit] if digit <= 3 else roman[5 * digit]
        number -= digit * (10 ** (i - 1))
    return result

