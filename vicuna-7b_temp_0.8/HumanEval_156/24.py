
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
    roman = []
    rem = 0
    while number > 0:
        digit = number % 10
        roman.append(get_roman_numeral_char(digit, rem))
        rem = (rem + 1) % 26
        number //= 10
    return ''.join(roman)
