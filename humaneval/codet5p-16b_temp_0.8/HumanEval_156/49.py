
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

    if not (1 <= number <= 1000):
        raise ValueError("Input must be between 1 and 1000")

    roman = ""

    # Numbers from 1 to 1000 are written out in "standard" roman numerals.
    # The 10s are "X", the 100s are "C", etc.
    # For example, the number 4 is "IIII", the number 9 is "VIIII", and the number 59 is "LIX".
    tens = number // 10
    ones = number % 10
    roman = ""
    if tens == 4:
        roman = roman + "XL"
    elif tens == 9:
        roman = roman + "XC"
    elif tens == 40:
        roman = roman + "XL"
    elif tens == 90:
        roman = roman + "XC"
    elif tens == 40:
        roman = roman + "XL"
    elif tens == 90:
        roman = roman + "XC"
    elif tens == 50:
        roman = roman + "L"
    elif tens == 90:
