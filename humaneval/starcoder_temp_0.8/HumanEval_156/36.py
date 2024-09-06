
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
    if type(number) is not int:
        raise TypeError("number must be int")
    if number < 1 or number > 1000:
        raise ValueError("number must be in range 1-1000")
    if number in number_to_roman_mini:
        return number_to_roman_mini[number]
    return int_to_roman(number)

