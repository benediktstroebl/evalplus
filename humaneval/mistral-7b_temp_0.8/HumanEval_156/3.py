
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
    # POSITIVE INTEGER CONVERSION TABLE
    # 1, 'I'
    # 2, 'II'
    # 3, 'III'
    # 4, 'IV'
    # 5, 'V'
    # 6, 'VI'
    # 7, 'VII'
    # 8, 'VIII'
    # 9, 'IX'
    # 10, 'X'

    # NUMBER CONVERSION TABLE
    # 0, ' '
    # 1, 'i'
    # 2, 'ii'
    # 3, 'iii'
    # 4, 'iv'
    # 5, 'v'
    # 6, 'vi'
    # 7, 'vii'
    # 8, 'viii'
    # 9, 'ix'
    # 10, 'x'
    # 20, 'xx'
    # 30, 'xxx'
    # 40, 'xl'
    # 50, 'lx
