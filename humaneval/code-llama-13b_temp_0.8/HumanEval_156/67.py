
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
        raise ValueError("number must be between 1 and 1000, inclusive")
    roman_nums = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
    roman_nums2 = ['x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc', 'c']
    roman_nums3 = ['c', 'cc', 'ccc', 'cd', 'd', 'dm', 'dcc', 'dccc', 'cm', 'm']
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    d = dict(zip(nums, roman_nums))
    d2 = dict(zip(nums, roman_nums2))
    d3 = dict(zip(nums, roman_nums3))
    num_digits = []
    while number != 0:
        num_digits.append(number % 10)
        number = number // 10
    mini_roman = ''
    num_digits.reverse()
    for digit in num_digits:
        if digit == 0:
            continue
        elif digit == 1:
            mini_roman += d[digit]
        elif digit == 2:
            mini_roman += d2[digit]
        elif digit == 3:
            mini_roman += d3[digit]
        elif digit == 4:
            mini_roman += d2[digit] + d[1]
        elif digit == 5:
            mini_roman += d3[digit]
        elif digit == 6:
            mini_roman += d3[digit] + d[1]
        elif digit == 7:
            mini_roman += d3[digit] + d2[1]
        elif digit == 8:
            mini_roman += d3[digit] + d[1]
        else:
            mini_roman
