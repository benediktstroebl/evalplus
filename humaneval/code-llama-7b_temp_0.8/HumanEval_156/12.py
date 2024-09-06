
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

    digits = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]

    if number < 0:
        raise ValueError

    if number > 3999:
        raise ValueError

    if number == 0:
        return ''

    result = ''
    for i in range(len(digits)):
        count = number // digits[i]
        if count > 0:
            result += str(roman[i] * count)
            number -= digits[i] * count
    return result
