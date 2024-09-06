
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

    roman = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
    result = ''
    while number:
        digit = number % 10
        if digit not in (9, 4, 5, 1):
            result += roman[digit]
        elif digit == 4:
            result += roman[4] + roman[digit]
        elif digit == 9:
            result += roman[9] + roman[digit]
        else:
            result += roman[5] + roman[1] * (digit - 5)
        number //= 10
    return result[::-1]

