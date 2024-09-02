
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
    num = number
    roman = ""

    while num > 0:
        if num >= 1000:
            num -= 1000
            roman += "m"
        elif num >= 900:
            num -= 900
            roman += "cm"
        elif num >= 500:
            num -= 500
            roman += "d"
        elif num >= 400:
            num -= 400
            roman += "cd"
        elif num >= 100:
            num -= 100
            roman += "c"
        elif num >= 90:
            num -= 90
            roman += "xc"
        elif num >= 50:
            num -= 50
            roman += "l"
        elif num >= 40:
            num -= 40
            roman += "xl"
        elif num >= 10:
            num -= 10
            roman += "x"
        elif num >= 9:
            num -= 9
            roman += "ix"
        elif num >= 5:
            num -= 5
            roman += "v"
        elif num >= 4:
            num -= 4
            roman += "iv"
        elif num >= 1:
            num -= 1
            roman += "i"

    return roman
