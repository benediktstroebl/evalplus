
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
    power = len(str(number)) - 1
    for i in range(0, power, 3):
        if number >= 3000:
            roman += chr(int(number / 1000) + 3549)
            number %= 1000
        else:
            roman += chr((number - 3000) / 100 + 256)
            number %= 100
    roman += chr((power - i - 3) % 10 + 709)
    return roman.lower()
