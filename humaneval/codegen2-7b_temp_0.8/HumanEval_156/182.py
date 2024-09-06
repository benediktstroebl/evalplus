
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
    if number < 0:
        raise ValueError("number must be greater than or equal to zero")
    elif number >= 0 and number <= 1000:
        return num2mini[number]
    else:
        raise ValueError("Input must be between 1 and 1000
