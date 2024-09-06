
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
        numerator = number % 1000
        denominator = number // 1000
        number = denominator
        numerator_digit = "M" if numerator > 100 else "X" if numerator > 9 else "I"
        roman = numerator_digit + roman[1] + str(numerator)
        if denominator > 100:
            denominator_digit = "C" if denominator > 100 else "D"
            denom_roman = denominator_digit + roman[2]
            roman = denom_roman + roman[0]
        else:
            denom_roman = "0" + roman[2]
            roman = denom_roman + roman[1]
    return roman.lower()
