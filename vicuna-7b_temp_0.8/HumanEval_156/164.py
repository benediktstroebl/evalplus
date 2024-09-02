
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
    roman_table = {
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
    numeral = numeral[numeral.count(' ') + 1:].lower()
    numeral_index = 0
    roman_result = ''
    for char in numeral:
        roman_result += roman_table.get(str(ord(char) - 48), '')
        numeral_index += 1

    return roman_result + roman_table.get(str(numeral_index), '')
