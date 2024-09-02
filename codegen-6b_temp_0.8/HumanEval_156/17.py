
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
    if not 1 <= number <= 1000:
        raise ValueError('number must be between 1 and 1000')

    # convert number to an array of integers
    def int_to_list(number):
        result = []
        for x in range(5):
            if number >= 1000:
                digit = number % 1000
                number //= 1000
                result.append(digit)
            else:
                result.append(number)
                break

        return result

    # convert each integer to an equivalent roman numeral
    def int_to_roman(numeral, value):
        ROMAN_NUMERALS = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
            10: 'X',
            20: 'XX',
            30: 'XXX',
            40: 'XL',
            50: 'L',
            60: 'LX',
            70: 'LXX',
            80: 'LXXX',
            90: 'XC',
            100: 'C',
            200: 'CC',
            300: 'CCC',
            400: 'CD',
            500: 'D',
            600: 'DC',
            700: 'DCC',
            800: 'DCCC',
            900: 'CM',
            1000: 'M'
        }
        index = 0
        roman_numeral = ''
        while numeral > 0:
            digit = numeral % value
            numeral //= value
            index += 1
            if digit == 9:
                roman_numeral = ROMAN_NUMERALS[value] + roman_numeral
            elif digit == 4:
                roman_numeral = ROMAN_NUMERALS[value / 10 * 10] + roman_numeral
            elif digit > 5:
                roman_numeral = ROMAN_NUMERALS[value / 10 * 10] + ROMAN_NUMERALS[value % 10] + roman_numeral
            else:
                roman_numeral = ROMAN_