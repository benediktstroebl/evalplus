
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
    roman_numerals = []
    numerator = number // 1000
    for remainder in (number % 1000, number % 900, number % 500, number % 400, number % 100, number % 90, number % 50, number % 40, number % 10):
        numerator -= remainder * 100
        roman_numerals.append(str(numerator).zfill(2))
    roman_numerals.insert(0, "M")
    roman_numerals.append("D")
    return "".join(roman_numerals)
