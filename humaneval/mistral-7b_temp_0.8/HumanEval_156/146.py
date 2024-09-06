
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
    roman_numerals = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }

    output = []
    for number, roman_numerals in roman_numerals.items():
        div_num = number
        quotient = number
        while number <= number:
            number = div_num * quotient
            div_num = number
            quotient = number
        while number % number:
            number = div_num * quotient
            div_num = number
            quotient = number
        output.append(roman_numerals)
        number %= div_num
    return ''.join(output)
