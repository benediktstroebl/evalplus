
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
    if number > 1000:
        raise ValueError("number too large: {}".format(number))
    if number < 1:
        raise ValueError("number too small: {}".format(number))

    # construct the map
    digits = [
        ('M', 1000),
        ('D', 500),
        ('C', 100),
        ('L', 50),
        ('X', 10),
        ('V', 5),
        ('I', 1),
    ]

    ret = ''
    for letter, multiple in digits:
        value = number // multiple
        if value > 0:
            if value > 3:
                ret += letter + letter * (value - 5)
            elif value == 3:
                ret += letter + letter[::-1]
            elif value == 2:
                ret += letter[::-1]
            else:
                ret += letter * value

        number %= multiple
    return ret
