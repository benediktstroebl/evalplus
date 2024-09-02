
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
    if type(number)!= int:
        raise ValueError("Input must be a positive integer")
    elif number < 1 or number > 1000:
        raise ValueError("Input must be in the range [1, 1000]")
    return roman_converter[number]
