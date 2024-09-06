
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
    if number > 1000:
        raise ValueError

    roman = ''
    i = 1
    while number != 0:
        if number >= i:
            roman += 'V' * (number//i)
            number %= i
        if number >= i:
            roman += 'X' * (number//i)
            number %= i
        if number >= i:
            roman += 'I' * (number//i)
            number %= i
        i *= 10
    return roman
