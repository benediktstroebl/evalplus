
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

    if not isinstance(number, int):
        raise TypeError("Invalid input.")
    if number < 1 or number > 1000:
        raise ValueError("Number must be within 1 and 1000.")
    nums = ['', 'M', 'MM', 'MMM']
    romans = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    return nums[number // 1000] + romans[number % 10]
