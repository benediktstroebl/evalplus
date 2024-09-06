
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
    one = 'i'
    five = 'v'
    ten = 'x'
    fifty = 'l'
    hundred = 'c'
    roman_numerals = [
        hundred + hundred,
        fifty + fifty,
        hundred,
        fifty,
        ten + ten,
        ten,
        one + one + one,
        one + one,
        one
    ]
    if number < 1 or number > 1000:
        raise ValueError("number must be between 1 and 1000")
    i = 0
    roman_number = ''
    while number > 0:
        while number >= len(roman_numerals):
            number -= 10 * (len(roman_numerals) - 1)
            roman_number += roman_numerals[len(roman_numerals) - 1]
        if number >= 9:
            roman_number += roman_numerals[0]
            number -= 10
        elif number >= 5:
            if i < 4:
                roman_number += five
            else:
                roman_number += one + roman_numerals[i - 1]
            number -= 5
        elif number >= 4:
            roman_number += one + one + roman_numerals[i]
            number -= 4
        elif number >= 2:
            roman_number += roman_numerals[i]
            number -= 2
        elif number == 1:
            roman_number += one
            number -= 1
        i += 1
    return roman_number.lower()
