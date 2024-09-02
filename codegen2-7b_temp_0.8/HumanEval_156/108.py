
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
    if number < 1 or number > 1000:
        raise ValueError("Input number must be between 1 and 1000")

    result = ""

    if number >= 1000:
        result += "m" * (number // 1000)
        number %= 1000

    if number >= 900:
        result += "c" + int_to_mini_roman(number % 900)
        number %= 900

    result += "x" * (number // 100)
    number %= 100

    return result + "v" * (number %
