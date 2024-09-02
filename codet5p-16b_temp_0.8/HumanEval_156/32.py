
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

    def get_value(value):
        """
        Return the roman numeral equivalent for a positive integer
        Restrictions: 1 <= num <= 1000

        Examples:
        >>> get_value(1) == 'i'
        >>> get_value(2) == 'ii'
        >>> get_value(3) == 'iii'
        >>> get_value(4) == 'iv'
        >>> get_value(5) == 'v'
        >>> get_value(6) == 'vi'
        >>> get_value(7) == 'vii'
        >>> get_value(9) == 'ix'
        >>> get_value(10) == 'x'
        """
        return {
            1: 'i',
            5: 'v',
            10: 'x',
            50: 'l',
            100: 'c',
            500: 'd',
            1000:'m'
        }[value]

    def get_num_to_str(number):
        """
        Return the roman numeral equivalent for a positive integer
        Restrictions: 1 <=
