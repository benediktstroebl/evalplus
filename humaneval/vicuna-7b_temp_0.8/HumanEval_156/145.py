
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

    numeral_parts = []

    for num in range(number):
        numeral_parts.append(str(num))

    numeral_string = ''.join(numeral_parts)

    for numeral, roman in roman_numerals.items():
        numeral_parts = [numeral]
        numeral_string = ''.join(numeral_parts)
        if number >= 100 and number not in [100, 200]:
            numeral_string = roman + numeral_string
        elif number in [100, 200]:
            numeral_parts = [roman]
            numeral_string = ''.join(numeral_parts)
            if number == 100:
                numeral_string += numeral_string[1:]
            elif number == 200:
                numeral_string += 'A'
            elif number >= 300 and number <= 399:
                numeral_string += 'V'
            elif number >= 400 and number <= 499:
                numeral_string += 'I'
            elif number >= 500 and number <= 599:
                numeral_string += 'X'
            elif number >= 600 and number <= 699:
                numeral_string += 'L'
            elif number >= 700 and number <= 799:
                numeral_string += 'XL'
            elif number >= 800 and number <= 899:
                numeral_string += 'L'
            elif number >= 900 and number <= 999:
