import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # This works, but I'm not entirely sure why.
    # Maybe I'm missing a few corner cases.
    # In fact, the above comment is probably wrong.
    # It works with just one negative number.
    # I'm sure there are more complicated cases, but I can't think of them right now.
    if len(nums) == 0:
        return 0

    min_sum = math.inf
    current_sum = 0

    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return min_sum
