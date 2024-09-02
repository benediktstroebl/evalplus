
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
    def tens_digit_converter(number):
        roman_numerals = {
            9: 'ix',
            5: 'v',
            4: 'iv',
            1: 'i'
        }
        if number < 10:
            return roman_numerals[number]
        if number == 10:
            return 'x'
        if number >= 10:
            return 'x' + tens_digit_converter(number - 10)

    def hundreds_digit_converter(number):
        roman_numerals = {
            9: 'xc',
            5: 'l',
            4: 'xl',
            1: 'c'
        }
        if number < 10:
            return roman_numerals[number]
        if number == 10:
            return 'x'
        if number >= 10:
            return 'x' + hundreds_digit_converter(number - 10)

    def converter(number):
        if number == 0:
            return ''
        if number <= 3:
            return 'i' * number
        if number == 4:
            return 'iv'
        if number == 5:
            return 'v'
        if number <= 8:
            return 'v' + converter(number - 5)
        if number == 9:
            return 'ix'

    tens_digit = number % 100
    hundreds_digit = number % 1000 // 100
    ones_digit = number % 1000 % 10
    roman_numeral = (
        hundreds_digit_converter(hundreds_digit) +
        tens_digit_converter(tens_digit) +
        converter(ones_digit)
    )
    return roman_numeral.lower()

