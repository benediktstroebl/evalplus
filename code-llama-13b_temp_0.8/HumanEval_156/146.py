
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
        raise ValueError("number must be between 1 and 1000")
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    roman_rep = ''
    for i in range(0, 13, 2):
        count = number // nums[i]
        if count:
            if nums[i+1] <= number < nums[i] * 5:
                if nums[i+1] == nums[i] * 2:
                    roman_rep += romans[i] + romans[i+1] * (count-1)
                else:
                    roman_rep += romans[i] + romans[i+1] + romans[i] * (count-1)
            else:
                roman_rep += romans[i] * count
            number %= nums[i]
    return roman_rep.lower()

