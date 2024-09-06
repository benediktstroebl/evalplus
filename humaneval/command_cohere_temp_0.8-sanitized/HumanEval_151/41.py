def double_the_difference(nums):
    "Returns the sum of squares of odd integers in nums, or 0 if empty."
    result = 0
    for n in nums:
        if isinstance(n, int) and n > 0:
            result += n**2
    return result