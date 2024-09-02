
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
    num_list = [1, 5, 10, 50, 100, 500, 1000]
    roman_nums = ['i', 'v', 'x', 'l', 'c', 'd', 'm']
    output = ""
    for i in range(len(num_list)):
        while num_list[i] <= number:
            output += roman_nums[i]
            number -= num_list[i]
    return output









































































































































