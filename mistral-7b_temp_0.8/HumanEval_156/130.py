
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
    roman_nums = ['i', 'v', 'x', 'l', 'c', 'd', 'm']
    roman_values = [1, 5, 10, 50, 100, 500, 1000]
    roman = []
    index = len(roman_nums) - 1
    while number > 0:
        while number >= roman_values[index]:
            number -= roman_values[index]
            roman.append(roman_nums[index])
        index -= 1
    return ''.join(reversed(roman))
