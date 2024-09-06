
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
    numerator = number // 1000
    denominator = number % 1000
    numerator_str = "M" + str(numerator).zfill(2)
    denomenator_str = "C" + str(denominator).zfill(2)
    result_str = numerator_str + "." + denomenator_str
    result_lower = result_str.lower()
    return result_lower
