
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
    roman = ''
    while number > 0:
        numerator = number / 1000
        number = number % 1000
        denominator = 10
        while denominator > 0:
            numerator = numerator // 10
            denominator = denominator // 10
        digit = numerator + denominator
        roman = (roman + 'M' + str(digit).zfill(2)).rstrip('M')
    return roman.lower()
