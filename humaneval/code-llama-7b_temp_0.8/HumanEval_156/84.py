
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
    result = ""

    # 1000 = M
    if number // 1000:
        result += "m" * (number // 1000)
        number %= 1000

    # 100 = C
    if number // 100:
        result += "c" * (number // 100)
        number %= 100

    # 10 = X
    if number // 10:
        result += "x" * (number // 10)
        number %= 10

    # 1 = I
    if number:
        result += "i" * (number // 1)
        number %= 1

    return result
