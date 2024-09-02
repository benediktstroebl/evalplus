
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
    if type(number) is not int:
        raise TypeError("expected int, got %s" % type(number))
    if number < 1 or number > 1000:
        raise ValueError("number %d is not between 1 and 1000" % number)

    # 1000
    thousand = number // 1000
    number -= thousand * 1000
    roman = 'm' * thousand

    # 100
    hundred = number // 100
    number -= hundred * 100
    if hundred <= 3:
        roman += 'c' * hundred
    else:
        roman += 'd' + 'c' * (hundred - 5)

    # 10
    ten = number // 10
    number -= ten * 10
    if ten == 9:
        roman += 'xci'
        number = 0
    elif ten <= 3:
        roman += 'x' * ten
    else:
        roman += 'l' + 'x' * (ten - 5)

    # 1
    if number == 0:
        return roman

    if number == 4:
        roman += 'iv'
        number = 0
    elif number == 9:
        roman += 'ix'
        number = 0
    elif number <= 3:
        roman += 'i' * number
    else:
        roman += 'v' + 'i' * (number - 5)

    return roman
