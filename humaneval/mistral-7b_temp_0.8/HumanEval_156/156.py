
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
    assert 0 <= number <= 1000

    symbols = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    res = []
    while number > 0:
        for key in symbols.keys():
            if number >= key:
                if key in (1, 5, 10, 50, 100, 500):
                    res.append(symbols[key])
                elif key in (100, 500, 1000):
                    res.append(symbols[key])
                    number -= key
                elif key in (5, 10, 50, 100, 500, 1000):
                    res.append(symbols[key])
                    number -= key
                else:
                    number -= key
                   
