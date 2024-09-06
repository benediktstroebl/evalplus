
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
        roman_digits = (
            '','m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i'
        )
        roman = ''
        while number > 0:
            roman += roman_digits[number % 10]
            number //= 10
        return roman.lower()
    else:
        raise ValueError('value must be between 1 and 1000
