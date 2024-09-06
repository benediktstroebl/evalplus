
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
    # 1000: M
    # 900: CM
    # 500: D
    # 400: CD
    # 100: C
    # 90: XC
    # 50: L
    # 40: XL
    # 10: X
    # 9: IX
    # 5: V
    # 4: IV
    # 1: I
    roman_numeral = ""
    divisor = 1000
    while number:
        if number >= divisor:
            roman_numeral += "M"
            number -= divisor
        divisor /= 10
        if number >= divisor:
            roman_numeral += "C"
            number -= 100
        divisor /= 10
        if number >= divisor:
            roman_numeral += "D"
            number -= 10
        divisor /= 10
        if number >= divisor:
            roman_numeral += "C"
            number -= 1
        divisor /= 10
    return roman_numeral
