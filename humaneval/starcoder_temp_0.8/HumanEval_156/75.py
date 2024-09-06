
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
    roman += "x"*int(number/10)
    roman += "v"*int(number/5)
    roman += "l"*int(number/50)
    roman += "d"*int(number/500)
    roman += "c"*int(number/100)
    roman += "m"*int(number/1000)

    return roman
