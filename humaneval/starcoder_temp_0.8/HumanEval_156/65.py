
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
    mini_romans = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]
    thousands = ["", "m", "mm", "mmm"]
    ten_powers = ["", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"]
    ones = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]

    num_thousands = number // 1000
    num_ten_powers = (number % 1000) // 100
    num_ones = ((number % 1000) % 100) // 10
    num_tens = ((number % 1000) % 100) % 10

    mini_roman = mini_romans[num_thousands] + thousands[num_ten_powers] + ten_powers[num_ones] + ones[num_tens]

    return mini_roman

