
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
    roman = ""
    while number > 0:
        digit = number % 10
        if digit == 1:
            roman = "I" + roman
        elif digit == 2:
            roman = "II" + roman
        elif digit == 3:
            roman = "III" + roman
        elif digit == 4:
            roman = "IV" + roman
        elif digit == 5:
            roman = "V" + roman
        elif digit == 6:
            roman = "VI" + roman
        elif digit == 7:
            roman = "VII" + roman
        elif digit == 8:
            roman = "VIII" + roman
        elif digit == 9:
            roman = "IX" + roman
        number = number // 10
    return roman
