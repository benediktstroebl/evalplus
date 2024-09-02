
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
    s = ""
    if number >= 1000:
        return s
    if number >= 900:
        s += "CM"
        number -= 900
    if number >= 500:
        s += "D"
        number -= 500
    if number >= 400:
        s += "CD"
        number -= 400
    if number >= 900:
        s += "CM"
        number -= 900
    if number >= 500:
        s += "D"
        number -= 500
    if number >= 400:
        s += "CD"
        number -= 400
    if number >= 100:
        s += "C"
        number -= 100
    if number >= 90:
        s += "XC"
        number -= 90
    if number >= 50:
        s += "L"
        number -= 50
    if number >= 40:
        s += "XL"
        number -= 40
    if number >= 10:
        s += "X"
        number -= 10
    if number >= 9:
        s += "IX"
        number -= 9
    if number >= 5:
        s += "V"
        number -= 5
    if number >= 4:
        s += "IV"
        number -= 4
    if number >= 1:
        s += "I"
    return s.lower()

