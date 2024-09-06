
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
        'I', 'V', 'X', 'L', 'XL', 'XC', 'CD', 'C', 'D', 'CM', 'D', 'M', 'MM'
    ]
    numeral_list = []

    while number > 0:
        numeral = number % 1000
        if numeral >= 100:
            numeral_list.append(roman_numerals[numeral - 100])
        number = number // 100

    return ' '.join(numeral_list)
