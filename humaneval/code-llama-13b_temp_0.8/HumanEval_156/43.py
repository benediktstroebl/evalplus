
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
    def mini_roman(number):
        if not isinstance(number, int) or number < 1 or number > 1000:
            raise ValueError("number must be between 1 and 1000")

        roman_numeral_map = (
            (1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'),
            (90, 'xc'), (50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'),
            (5, 'v'), (4, 'iv'), (1, 'i'),
        )
        result = ""
        for arabic, roman in roman_numeral_map:
            if number < arabic:
                continue
            result += roman * (number // arabic)
            number = number % arabic
        return result

    if number < 1 or number > 1000:
        raise ValueError("number must be between 1 and 1000")

    if number >= 100:
        return mini_roman(number)

    if number < 10:
        if number == 9:
            return "ix"
        if number == 5:
            return "v"
        if number == 4:
            return "iv"
        if number < 5:
            return "i" * number

    if number == 15:
        return "v" + "i" * 4
    if number == 40:
        return "x" + "l"
    if number == 90:
        return "x" + "c"
    if number == 400:
        return "cd" + "i" * 4
    if number == 900:
        return "cm" + "i" * 4

    if number < 40:
        return "l" + "x" * (number - 50)
    if number < 90:
        return "c" + "d" + "x" * (number - 50)
