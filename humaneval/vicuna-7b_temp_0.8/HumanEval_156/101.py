
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
    if number == 0:
        return '0'
    if number < 1000:
        return str(number)[2:].zfill(2)
    elif number < 10000:
        return str(number)[1:].zfill(1)
    else:
        if number < 100000:
            return 'M', 'CM', 'D'
        elif number < 1000000000:
            return 'MM', 'CD', 'C'
        else:
            return 'XC', 'L', 'XL'
