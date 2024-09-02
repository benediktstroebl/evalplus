
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
    M = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    m = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    str_number = []
    i = 0
    while number > 0:
        if number - m[i] >= 0:
            str_number.append(M[i])
            number = number - m[i]
        i = i + 1
    return ''.join(str_number)


