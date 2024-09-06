
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
    digits = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = ""
    i = 0
    while number > 0:
        count = number // digits[i]
        number -= count * digits[i]
        if count < 4:
            result += romans[i] * count
        else:
            result += romans[i + 1]
            if count >= 5 and i != 2:
                result += romans[i - 1]
            elif i == 2:
                result += "CM"
        i += 1

    return result.lower()

