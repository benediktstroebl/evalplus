
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
    if not 1 <= number <= 1000:
        raise ValueError("number must be between 1 and 1000.")

    roman_nums = ["i", "v", "x", "l", "c", "d", "m"]
    roman_values = [1, 5, 10, 50, 100, 500, 1000]

    mini_roman = ""
    i = len(roman_values) - 1
    while number > 0:
        if number >= roman_values[i]:
            mini_roman += roman_nums[i]
            number -= roman_values[i]
        else:
            i -= 1

    return mini_roman
