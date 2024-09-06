import unittest
def int_to_mini_roman(n):
    if n < 1:
        return ""
    num_str = str(n).replace("iv", "ii").replace("ix", "x").replace("xl", "x").replace("xc", "x").replace("iv", "ii")
    nums, romans = [], []
    for c in num_str:
        if c.isdigit():
            nums.append(c)
        else:
            romans.append(c)
    roman_nums = "".join(nums)
    result = nums + roman_nums
    return result