
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

    if not isinstance(number, int) or number <= 0 or number > 1000:
        return "Error: Number must be between 1 and 1000"

    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = []
    for i in range(len(values)):
        count = number // values[i]
        result.append(numerals[i] * count)
        number -= values[i] * count
    return "".join(result)
