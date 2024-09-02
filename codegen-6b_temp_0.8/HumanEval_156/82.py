
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
    if 1 > number or number > 1000:
        raise ValueError("Invalid integer: {}".format(number))
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ['', 'm', 'cm', 'd', 'cd', 'c', 'x', 'l', 'xl', 'm', 'ix', 'v', 'iv','i']
    index = 0
    while number > 0:
        value = nums[index]
        while value < number:
            index += 1
        answer = romans[index]
        number -= value
    return answer.lower()
