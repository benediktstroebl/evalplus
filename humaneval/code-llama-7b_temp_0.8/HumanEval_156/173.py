
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

    conversions = {
        1000 : 'm',
        500  : 'd',
        100  : 'c',
        10   : 'x',
        5    : 'v',
        1    : 'i',
    }

    def int_to_roman(n):
        """
        >>> int_to_roman(10)
        'x'
        >>> int_to_roman(5)
        'v'
        >>> int_to_roman(1)
        'i'
        """
        for value, letter in conversions.items():
            while n >= value:
                yield letter
                n -= value
    return ''.join(int_to_roman(number)).lower()

