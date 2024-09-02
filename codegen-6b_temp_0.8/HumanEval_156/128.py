
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
    assert number >= 1 and number <= 1000, 'Invalid Input'

    romans = ('','I','II','III','IV','V','VI','VII','VIII','IX', 'X', 'XX',
              'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C', 'CC', 'CCC',
              'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
    res = ''
    while number:
        res += romans[number % 10]
        number //= 10
    return res.lower()

