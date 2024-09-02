
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
    hundreds = ["", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"]
    tens = ["", "x", "xx", "xxx", "l", "lx", "ll", "llx", "lll", "xc"]
    ones = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]
    result = []
    if number >= 100:
        result.append(hundreds[number//100])
    if number % 100 >= 10:
        result.append(tens[number//10 % 10])
    if number % 10 != 0:
        result.append(ones[number % 10])
    return ''.join(result)

