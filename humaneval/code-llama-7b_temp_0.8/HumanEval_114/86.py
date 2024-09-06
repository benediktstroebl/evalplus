import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_sum = math.inf
    sub_sum = 0
    for num in nums:
        sub_sum += num
        min_sum = min(min_sum, sub_sum)
        if sub_sum < 0:
            sub_sum = 0

    return min_sum
