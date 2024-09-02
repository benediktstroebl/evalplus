
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


    romans = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}

    if number < 1:
        return "Error"

    if number <= 10:
        return romans.keys()[number-1]

    out = romans.keys()[number-1]

    while number > 1:
        if number >= 5:
            number -= 5
            out += romans.keys()[1]
        elif number >= 4:
            number -= 4
            out += romans.keys()[0] + romans.keys()[1]
        elif number >= 3:
            number -= 3
            out += romans.keys()[0] + romans.keys()[0]
        elif number >= 2:
            number -= 2
            out += romans.keys()[0] + romans.keys()[1]
        elif number >= 1:
