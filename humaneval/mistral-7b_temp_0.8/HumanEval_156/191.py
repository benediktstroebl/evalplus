
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
    assert number <= 1000, 'number is not in range [1, 1000]'
    rom_digits = 'I', 'V', 'X', 'L', 'C', 'D', 'M'
    nums = '1', '5', '10', '50', '100', '500', '1000'
    r_nums = rom_digits, rom_digits[1:3], rom_digits[2:4], rom_digits[3:5], rom_digits[4:6], rom_digits[5:7], rom_digits[6:]
    r_d_nums = nums, nums[1:3], nums[2:4], nums[3:5], nums[4:6], nums[5:7], nums[6:]
    res = ''
    for i in range(len(nums)):
        while number >= r_d_nums[i]:
            number -= int(r_d_nums[i])
            res
