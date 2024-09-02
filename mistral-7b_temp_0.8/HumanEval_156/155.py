
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

    romans = ["I", "V", "X", "L", "C", "D", "M", "I", "V", "X", "L", "C", "D", "M", "I", "V", "X", "L", "C", "D", "M"]
    roman_nums = [1, 5, 10, 50, 100, 500, 1000, 1, 5, 10, 50, 100, 500, 1000, 1, 5, 10, 50, 100, 500, 1000]

    roman = ""
    while number > 0:
        i = 0
        while number >= roman_nums[i]:
            roman += romans[i]
            number -= roman_nums[i]
            i += 1

    return roman

