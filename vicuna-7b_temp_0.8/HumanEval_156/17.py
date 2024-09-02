
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
        'I': '1',
        'V': '5',
        'X': '10',
        'L': '50',
        'C': '100',
        'D': '500',
        'M': '1000'
    }

    if number >= 4000:
        return roman_numerals[number - 4000] + roman_numerals[number - 3000] + roman_numerals[number - 2000] + roman_numerals[number - 1000]

    numerator = number // 1000
    denominator = number
    numerator_i = 1000
    for i in range(1000):
        denominator_i = denominator // 1000
        numerator_i += 1
        numerator_i = (numerator_i % 10) + (numerator_i / 10) * roman_numerals['M']
        numerator = numerator * roman_numerals['X'] + numerator_i
        if denominator_i == 1:
            break
    return roman_numerals[numerator] + str(numerator_i)
