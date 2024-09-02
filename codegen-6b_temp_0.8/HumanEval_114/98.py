import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    if n == 1:
        return nums[0]
    min_sum = -math.inf
    for start in range(n):
        if start == 0:
            curr_sum = nums[start]
        else:
            curr_sum += nums[start]
        if curr_sum >= 0:
            min_sum = min(min_sum, curr_sum)
    return min_sum

