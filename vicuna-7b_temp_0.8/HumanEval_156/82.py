
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
        digit = number % 1000
        if digit >= 400:
            roman += 'CD'
            number /= 1000
        elif digit >= 300:
            roman += 'C'
            number /= 1000
        elif digit >= 200:
            roman += 'X'
            number /= 1000
        else:
            digit -= 400
            roman += 'X' if digit > 0 else 'I'
            number /= 1000
        number = number / 1000
    return roman.lower()
