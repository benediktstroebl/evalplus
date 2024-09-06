
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
    roman = []
    carry = 0

    for i in range(len(str(number))):
        digit = str(number)[i]
        numeral = get_numeral(digit)
        value = numeral.value + carry
        carry = value / 1000
        value = value % 1000
        roman.append(roman_digit(value, i))

    return ''.join(roman)
