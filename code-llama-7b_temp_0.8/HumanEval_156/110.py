
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
    # All roman numeral conversions are done as long as the input is larger than
    # 10. So, the base case is 10.
    if number <= 10:
        return _mini_roman(number)

    # For the recursive case, we have to subtract the current number by its
    # conversion.
    return int_to_mini_roman(number - 10) + _mini_roman(10)

