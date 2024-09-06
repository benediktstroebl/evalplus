
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
    roman_equivalent = ""
    one = "i"
    five = "v"
    ten = "x"
    fifty = "l"
    hundred = "c"
    roman_equivalent += (number // 100) * hundred
    if number % 100 >= 90:
        roman_equivalent += "x"
        number %= 90
    if number % 100 >= 50:
        roman_equivalent += fifty
        number %= 50
    if number % 100 >= 40:
        roman_equivalent += ten
        number %= 40
    if number % 100 >= 10:
        roman_equivalent += ten
        number %= 10
    if number % 10 >= 9:
        roman_equivalent += one
        number %= 9
    if number % 10 >= 5:
        roman_equivalent += five
        number %= 5
    if number % 10 >= 4:
        roman_equivalent += one
        number %= 4
    if number % 10 >= 2:
        roman_equivalent += one
        number %= 2
    if number % 10 >= 1:
        roman_equivalent += one
        number %= 1
    return roman_equivalent

