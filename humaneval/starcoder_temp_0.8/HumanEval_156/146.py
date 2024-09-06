
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
    # Decompose the problem into smaller problems and compose the result
    roman_numerals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    int_to_roman = {}
    roman_to_int = {}
    for i in range(len(roman_numerals)):
        int_to_roman[roman_numerals[i]] = roman_letters[i]
        roman_to_int[roman_letters[i]] = roman_numerals[i]

    # Execute the algorithm
    i = 0
    roman_numeral = ''
    while number > 0:
        if number - roman_numerals[i] >= 0:
            roman_numeral += int_to_roman[roman_numerals[i]]
            number -= roman_numerals[i]
        else:
            i += 1
    return roman_numeral

