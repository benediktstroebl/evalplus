
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
    if number > 3999:
        raise Exception("Number too large.")
    if number < 1:
        raise Exception("Number must be positive")
    roman = "m" * (number // 1000) + "d" * (number % 1000 // 500) + "c" * (
        number % 1000 % 500 // 100
    ) + "l" * (number % 1000 % 500 % 100 // 50) + "x" * (
        number % 1000 % 500 % 100 % 50 // 10
    ) + "v" * (number % 1000 % 500 % 100 % 50 % 10 // 5) + "i" * (
        number % 1000 % 500 % 100 % 50 % 10 % 5
    )
    return roman.lower()
