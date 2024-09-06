
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
    if 1 <= number <= 1000:
        symbol_map = {1: 'x', 5: 'l', 10: 'c', 50: 'd', 100: 'm', 500: '', 1000: ''}
        ret = ''
        # XXX: this is dumb... but works as expected when 10<=number<=1000
        while number:
            if number >= 1000:
                ret += symbol_map[1000]
                number -= 1000
            elif number >= 500:
                ret += symbol_map[500]
                number -= 500
            elif number >= 100:
                ret += symbol_map[100]
                number -= 100
            elif number >= 50:
                ret += symbol_map[50]
                number -= 50
            else:
                ret += symbol_map[10]
                number -= 10
        return ret
    else:
        raise ValueError("number out of bounds: 1 <= number <= 1000")

