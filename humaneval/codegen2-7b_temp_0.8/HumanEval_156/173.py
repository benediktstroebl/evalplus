
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
    roman_nums = ["", "i", "ii", "iii", "iv", "v", "vi", "vii"]
    string = ""
    for i in range(1, number + 1):
        string += roman_nums[(i // 1000) * 10] + roman_nums[i % 10]
    return string.lower()

