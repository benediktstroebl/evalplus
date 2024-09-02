
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

    mapping = [
        ['', '', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        ['', '', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['', '', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        ['', '', 'M', 'MM', 'MMM', '', '', 'MMMM', 'MMMMM', 'MMMMMM', ''],
    ]
    r, i, s = '', 1, 0
    while number > 0:
        q, r = number // 10, number % 10
        if q == 4:
            i += 1
            q = 9
        elif q == 9:
            i += 2
            q = 5
        else:
            i += 3
            q = q % 5
        s = mapping[i][q]
        r = mapping[i][r
