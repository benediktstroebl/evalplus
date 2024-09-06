
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
    if not (1 <= number <= 1000):
        raise ValueError('Invalid input')

    roman_nums = [
        ['i', 'v', 'x'],
        [1, 5, 10],
        [2, 5, 5],
        [3, 5, 1],
        [4, 5, 0],
        [5, 5, 0],
    ]

    return ''.join(numbers[i] for i in roman_nums[number - 1])

