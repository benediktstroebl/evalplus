
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

    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    thousands_idx = number // 1000
    number = number - (thousands_idx * 1000)

    hundreds_idx = number // 100
    number = number - (hundreds_idx * 100)

    tens_idx = number // 10
    number = number - (tens_idx * 10)

    ones_idx = number

    return thousands[thousands_idx] + hundreds[hundreds_idx] + tens[tens_idx] + ones[ones_idx]

