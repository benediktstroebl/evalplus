
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
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    numeral = str(number)
    result = []
    for i in range(len(numeral)):
        numeral_digit = numeral[i]
        power = 0
        while numeral_digit >= 10:
            numeral_digit -= 10
            power += 1
        value = numeral_digit
        for i in range(1, power):
            value = 5 + (value - 10 * 9) / 10
        result.append(roman_numerals.get(str(power), '0')) + value
    return ''.join(result)
