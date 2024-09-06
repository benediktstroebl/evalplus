
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

    roman_numerals = [
        '',
        'I',
        'II',
        'III',
        'IV',
        'V',
        'VI',
        'VII',
        'VIII',
        'IX'
    ]

    output = []

    count = 1

    while count <= number:
        if count >= 1 and count <= 10:
            output.append(roman_numerals[count])
        elif count == 11:
            output.append(roman_numerals[10] + roman_numerals[1])
        elif count >= 12 and count <= 20:
            output.append(roman_numerals[5] + roman_numerals[10])
        elif count == 30:
            output.append(roman_numerals[10] + roman_numerals[20])
        elif count >= 40 and count <= 50:
            output.append(roman_numerals[10] + roman_numerals[30])
        elif count == 90:
            output.append(roman_n
