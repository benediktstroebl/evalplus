
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
    if number < 1 or number > 1000:
        return ""
    roman = ''
    roman += 'M' * (number // 1000)
    number %= 1000
    roman += 'C' * (number // 100)
    number %= 100
    roman += 'D' * (number // 50)
    number %= 50
    roman += 'L' * (number // 10)
    number %= 10
    roman += 'X' * (number // 5)
    number %= 5
    roman += 'V' * (number // 1)
    number %= 1
    return roman
