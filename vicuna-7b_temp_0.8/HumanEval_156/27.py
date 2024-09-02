
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
    roman_numerals = [None, "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII",
                      "IV", "IX", "X", "XII", "CM", "D", "CXXV", "L", "XC", "XL", "L", "X", "V", "IV", "I"]
    result = [roman_numerals[number // 1000]]
    for remainder in number % 1000:
        result.append(roman_numerals[remainder])
    return "".join(result[::-1])
