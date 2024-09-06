
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
    ones = [None, 'i', 'x', 'c', 'm']
    tens = [None, 'x', 'xx', 'xxx', 'l', 'lx', 'lxx', 'lxxx', 'xc', 'cx', 'cxx', 'ccx', 'cd', 'd', 'dc', 'dcc', 'cm']
    number_of_digits = len(str(number))
    if number_of_digits == 1:
        return ones[number]
    elif number_of_digits == 2:
        if number % 10 == 0:
            return tens[number_of_digits - 1]
        else:
            return tens[number // 10] + ones[number % 10]
    elif number_of_digits == 3:
        if number % 10 == 0:
            return ones[number // 10] + tens[number_of_digits - 1]
        else:
            return ones[number // 100] + tens[number_of_digits - 1] + (ones[number % 10] if number % 10 != 0 else '')
    else:
        return ''
