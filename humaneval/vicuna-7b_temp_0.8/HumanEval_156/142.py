
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
    i = number
    while i > 0:
        if i == 1:
            roman = "I" + roman
        elif i == 2:
            roman = "II" + roman
        elif i == 3:
            roman = "III" + roman
        elif i == 4:
            roman = "IV" + roman
        elif i == 5:
            roman = "V" + roman
        elif i == 6:
            roman = "VI" + roman
        elif i == 7:
            roman = "VII" + roman
        elif i == 8:
            roman = "VIII" + roman
        elif i == 9:
            roman = "IX" + roman
        i = i - 1

    return roman
