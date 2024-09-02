
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
    def mini_roman_digit_to_str(digit):
        """
        Converts a digit to its roman numeral equivalent as a string,
        and return it in lowercase.
        Restrictions: 1 <= num <= 10

        Examples:
        >>> mini_roman_digit_to_str(1) == 'i'
        >>> mini_roman_digit_to_str(5) == 'v'
        >>> mini_roman_digit_to_str(6) == 'vi'
        """
        if digit < 4:
            return 'i' * digit
        elif digit == 4:
            return 'iv'
        elif 5 <= digit < 9:
            return 'v' + mini_roman_digit_to_str(digit - 5)
        elif digit == 9:
            return 'ix'

    if number < 1 or number > 1000:
        raise ValueError('number should be between 1 and 1000.')

    mini_roman = []
    for i in xrange(3, -1, -1):
        digit = number // 10**i
        number -= digit * 10**i
        mini_roman.append(mini_roman_digit_to_str(digit))
    return ''.join(mini_roman)

