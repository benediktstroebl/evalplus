
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
    if not (1 <= number <= 1000):
        raise ValueError("Accepted integers are in the range [1, 1000]")
    if number <= 10:
        return f"x{number}"
    elif number <= 20:
        return f"xx{number - 10}"
    elif number <= 100:
        return f"xix{number - 20}"
    else:
        return f"clix{number - 100
