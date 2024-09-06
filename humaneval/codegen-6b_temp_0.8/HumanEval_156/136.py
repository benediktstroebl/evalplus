
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
    r_1 = ["", "m", "cm", "d", "cd", "dC", "D", "dc", "Dc", "C", "cC", "Cc", "CC", "cCC", "CCC", "ccCC", "ccCCC", "cccdCC", "cccDCC", "cccDCCC", "cccCM"]
    r_2 = ["", "x", "X", "l", "L", "XL", "LX", "LXX", "LXXL", "LXXX", "LXXXL", "LXXXX", "LXXXXX", "LXXXXXX", "LXXXXXXX", "LFFFFFF"]
    r_3 = ["", "i", "I", "v", "V", "VV", "VVV", "VVVV", "VVVVV", "VVVVVV", "VVVVVVV", "VVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVVVVVVVV", "VVV