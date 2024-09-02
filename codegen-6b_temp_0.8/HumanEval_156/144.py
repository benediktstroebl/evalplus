
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
    def roman_numeral(value):
        """
        Given a positive integer, return a string that is the roman numeral
        equivalent.
        Restriction: 1 <= value <= 1000

        Examples:
        >>> roman_numeral(19) == 'xix'
        >>> roman_numeral(152) == 'clii'
        >>> roman_numeral(426) == 'cdxxvi'
        """
        adjacent = 1
        roman_string = ''
        for i, numeral in enumerate(sorted(roman_numeral_map.keys())):
            if numeral > value:
                continue
            if value % numeral == 0:
                value /= numeral
                roman_string += roman_numeral_map[numeral]
                adjacent = 1
            elif adjacent == 1:
                roman_string += roman_numeral_map[numeral]
                adjacent = 0
        return roman_string

    def recurse(num):
        """
        Recursively compute.
        Restriction: 1 <= num <= 1000
        """
        if num <= 1:
            return roman_numeral_map[num]
        if num % 100 == 0:
            return recurse(num / 100) + 'hundred'
        if num % 10 == 0:
            return roman_numeral_map[num / 10] + recurse(num % 10)
        return recurse(num / 10) + roman_numeral_map[num % 10]

    roman_numeral_map = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }
    return recurse(number)

