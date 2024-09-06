
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
    romans = ["i", "v", "x", "l", "c", "d", "m"]
    values = [1, 5, 10, 50, 100, 500, 1000]
    n = len(values)
    roman = ''
    while number > 0:
        for i in range(n):
            if values[i] <= number:
                number -= values[i]
                roman += romans[i]
                break

    return roman
