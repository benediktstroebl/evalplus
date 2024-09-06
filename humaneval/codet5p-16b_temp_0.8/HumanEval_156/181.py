
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

    def int_to_roman_symbol(number):
        '''
        Convert an integer to its roman numeral equivalent as a string,
        and return it in lowercase.
        Restrictions: 1 <= num <= 1000
        Examples:
        >>> int_to_roman_symbol(1) == 'i'
        >>> int_to_roman_symbol(2) == 'ii'
        >>> int_to_roman_symbol(3) == 'iii'
        >>> int_to_roman_symbol(4) == 'iv'
        >>> int_to_roman_symbol(5) == 'v'
        >>> int_to_roman_symbol(6) == 'vi'
        >>> int_to_roman_symbol(7) == 'vii'
        >>> int_to_roman_symbol(8) == 'viii'
        >>> int_to_roman_symbol(9) == 'ix'
        >>> int_to_roman_symbol(10) == 'x'
        >>> int_to_roman_symbol(20) == '
