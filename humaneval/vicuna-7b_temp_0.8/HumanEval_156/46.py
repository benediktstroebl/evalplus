
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
    while number > 0:
        digit = str(number % 100)
        if number > 100:
            digit = digit[1:] * 100 + number // 100
        while digit.startswith(("I", "V", "X", "L", "C", "D")):
            digit = digit[1:] * 10 + digit[0]
        roman.append(digit)
        number = number // 100
    return ''.join(roman)
